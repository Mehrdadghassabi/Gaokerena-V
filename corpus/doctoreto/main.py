from bs4 import BeautifulSoup
import requests
import re

def getHTMLdocument(url):
    response = requests.get(url)
    return response.text

def getQuestionlinks(url_to_scrape):
    links = set()
    for i in range(1,265):
        html_document = getHTMLdocument(url_to_scrape + str(i) + '/')
        soup = BeautifulSoup(html_document, 'html.parser')
        for link in soup.find_all('a',
                              attrs={'href': re.compile("^https://doctoreto.com/blog/")}):
            #if link.parent.name == 'article':
            links.add(link.get('href'))
    return links

def crawl_articles(links):
    count = 0
    for link in links:
        st = get_article_text(link)
        count += 1
        with open(str(count)+ ".txt", 'w') as file:
            if st is not None and st != "":
               file.write(st)
        print("Article has been written to " + str(count)+ ".txt")

def get_article_text(url):
    html_content = getHTMLdocument(url)
    soup = BeautifulSoup(html_content, 'html.parser')
    article = soup.find('div', class_ = "start-content")

    if article:
        return article.get_text(separator='\n', strip=True)
    else:
        return None

if __name__ == '__main__':
    links = getQuestionlinks('https://doctoreto.com/blog/all-posts/page/')
    crawl_articles(links)