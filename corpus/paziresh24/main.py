import requests
from bs4 import BeautifulSoup
import os
import re

save_path = "paziresh24"
os.makedirs(save_path, exist_ok=True)

sitemap_url = "https://www.paziresh24.com/blog/post-sitemap12.xml"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

response = requests.get(sitemap_url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "xml")

    article_links = [loc.text for loc in soup.find_all("loc") if not loc.text.startswith("https://www.paziresh24.com/blog/wp-content")]

    for link in article_links:
        try:
            article_response = requests.get(link, headers=headers)
            if article_response.status_code == 200:
                article_soup = BeautifulSoup(article_response.text, "html.parser")

                title_tag = article_soup.find("title")
                title = title_tag.text.strip() if title_tag else "article"

                title = re.sub(r'[\/:*?"<>|]', '_', title)

                title = title.split('_')[0]

                article_body = article_soup.select_one("div.entry-content")

                if article_body:
                    for cls in ["ez-toc-container-direction", "aiosrs-rating-wrap", "stream-item-below-post-content", "post-bottom-source"]:
                        for tag in article_body.find_all(class_=cls):
                            tag.decompose()

                    text = article_body.get_text(separator="\n", strip=True)

                    file_path = os.path.join(save_path, f"{title}.txt")
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(text)
                    
                    print(f"{title}.txt")
                else:
                    print(f"not found {link}")

        except Exception as e:
            print(f"{link}: {e}")

else:
    print(response.status_code)
