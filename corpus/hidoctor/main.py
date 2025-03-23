from bs4 import BeautifulSoup
import requests
import re

def getHTMLdocument(url):
    response = requests.get(url)
    return response.text

def getQuestionlinks(url_to_scrape):
    html_document = getHTMLdocument(url_to_scrape)
    soup = BeautifulSoup(html_document, 'html.parser')
    links = set()
    for link in soup.find_all('a',
                              attrs={'href': re.compile("^https://www.hidoctor.ir/")}):
        if link.parent.name == 'article':
           links.add(link.get('href'))
    return links

def crawl_articles(bgn,num_available_pages):
    count = 0
    for i in range(bgn,num_available_pages+1):
        links = getQuestionlinks('https://www.hidoctor.ir/page/'+str(i)+'/')
        for link in links:
            st = get_article_text(link)
            count += 1
            with open(str(i) + "_" + str(count)+ ".txt", 'w') as file:
                if st is not None:
                   file.write(st)
            print("Article has been written to " + str(i) + "_" + str(count)+ ".txt")

def get_article_text(url):
    html_content = getHTMLdocument(url)
    soup = BeautifulSoup(html_content, 'html.parser')
    article = soup.find('div', class_ = "post-content typography single-post-body clearfix progressive")

    if article:
        return article.get_text(separator='\n', strip=True)
    else:
        return None

if __name__ == '__main__':
    crawl_articles(bgn = 9952 ,num_available_pages = 14736)