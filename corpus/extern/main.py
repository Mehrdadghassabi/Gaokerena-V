import requests
from bs4 import BeautifulSoup
import os
import re

save_path = "extern"
os.makedirs(save_path, exist_ok=True)

sitemap_url = "https://extern.ir/extern_health-sitemap.xml"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

response = requests.get(sitemap_url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "xml")

    article_links = [loc.text for loc in soup.find_all("loc") if loc.text.startswith("https://extern.ir/health")]

    for link in article_links:
        try:
            article_response = requests.get(link, headers=headers)
            if article_response.status_code == 200:
                article_soup = BeautifulSoup(article_response.text, "html.parser")

                title_tag = article_soup.find("title")
                title = title_tag.text.strip() if title_tag else "article"

                title = re.sub(r'[\/:*?"<>|]', '_', title)

                title = title.split('_')[0]

                article_body = article_soup.select_one("div.paper__content")

                if article_body:
                    for unwanted in article_body.find_all([
                        "script", "style", "aside", "nav", "form", "footer", "header", "iframe", "noscript",
                        "video", "audio", "button", "input", "textarea", "svg", "link", "meta", "picture",
                        "figure", ".comments", ".comment", ".related-posts", ".advertisement", ".ad", ".popup",
                        ".sidebar", ".newsletter", ".social-share", ".breadcrumb", ".author-box", ".tags"
                    ]):
                        unwanted.decompose()

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
