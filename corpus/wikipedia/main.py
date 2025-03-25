import requests
import re
import os
from bs4 import BeautifulSoup
from urllib.parse import unquote


BASE_URL = "https://fa.wikipedia.org"

def get_article_links(page_url):
    response = requests.get(page_url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    links = []
    content = soup.find('div', {'class': 'mw-parser-output'})
    if content:
        for link in content.find_all('a', href=True):
            href = link['href']
            if href.startswith("/wiki/") and ":" not in href and "#" not in href: 
                links.append(href)
    
    return list(set(links)) 


def crawl_wikipedia(page_url, file_name):
    response = requests.get(page_url)
    if response.status_code != 200:
        print(f"error {page_url}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find('div', {'class': 'mw-parser-output'})
    
    if not content:
        print(f"no content: {page_url}")
        return
    
    text = ""
    ignore_titles = {"جستارهای وابسته", "منابع", "پیوند به بیرون"} 
    
    for element in content.find_all(['h2', 'h3', 'p']):
        if element.name in ['h2', 'h3']: 
            title = element.get_text().strip()
            title = re.sub(r'\[.*?\]', '', title) 
            if title in ignore_titles:
                continue  
            text += f"\n\n## {title}\n\n"
        elif element.name == 'p':  
            paragraph = element.get_text().strip()
            paragraph = re.sub(r'\[\d+\]', '', paragraph)  
            if paragraph:
                text += paragraph + "\n\n"

    with open(file_name, "w", encoding="utf-8") as file:
        file.write(text)
    
    print(file_name)


main_page = "https://fa.wikipedia.org/wiki/ویکی‌پدیا:مقاله‌های_حیاتی/بخش_پزشکی_و_سلامت"

article_links = get_article_links(main_page)

os.makedirs("articles", exist_ok=True)

for link in article_links:
    article_title = unquote(link.split("/")[-1])
    file_path = os.path.join("articles", f"{article_title}.txt") 
    crawl_wikipedia(BASE_URL + link, file_path)
