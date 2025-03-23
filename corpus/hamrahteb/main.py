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
    for div in soup.find_all('div',class_ = "post-content"):
       for link in div.find_all('a',
                              attrs={'href': re.compile("^https://hamrah-teb.com/blog/")}):
           links.add(link.get('href'))
    return links

def get_article_text(url):
    html_content = getHTMLdocument(url)
    soup = BeautifulSoup(html_content, 'html.parser')
    article = soup.find('div', class_ = "article-content text-justify")

    if article:
        return article.get_text(separator='\n', strip=True)
    else:
        return None

def crawl_articles(bgn,num_available_pages):
    count = 0
    for i in range(bgn,num_available_pages+1):
        links = getQuestionlinks('https://hamrah-teb.com/blogs?page='+str(i))
        for link in links:
            st = get_article_text(link)
            count += 1
            with open(str(count)+ ".txt", 'w') as file:
                if st is not None:
                   file.write(st)
            print("Article has been written to " + str(count)+ ".txt")

if __name__ == '__main__':
    crawl_articles(1, 53)