import httpx
from lxml import etree
from pathlib import Path
import re

save_path = Path("sallammag")
save_path.mkdir(exist_ok=True)

sitemap_url = "https://salammag.com/post-sitemap1.xml"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

response = httpx.get(sitemap_url, headers=headers, timeout=10)
response.raise_for_status()

root = etree.fromstring(response.content)
article_links = [loc.text for loc in root.findall(".//{*}loc") if not loc.text.startswith("https://salammag.com/wp-content")]

for link in article_links:
    article_response = httpx.get(link, headers=headers, timeout=10)
    article_response.raise_for_status()

    parser = etree.HTMLParser()
    tree = etree.fromstring(article_response.content, parser)

    title_tag = tree.find(".//title")
    title = title_tag.text.strip() if title_tag is not None else "article"
    title = re.sub(r'[\/:*?"<>|]', '_', title).split('_')[0]

    content_element = tree.xpath("//div[@class, 'content ']")
    if content_element:
        text = "\n".join(content_element[0].itertext()).strip()

        file_path = save_path / f"{title}.txt"
        file_path.write_text(text, encoding="utf-8")

        print(title)
