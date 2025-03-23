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
                              attrs={'href': re.compile("^https://www.darmankade.com/blog/")}):
        if link.parent.name == 'article':
           links.add(link.get('href'))
    return links

def crawl_articles(bgn):
    count = 0
    for i in range(bgn,22):
        links = getQuestionlinks('https://www.darmankade.com/blog/medicine/page/'+str(i)+'/')
        for link in links:
            st = get_article_text(link)
            count += 1
            with open(str(count)+ ".txt", 'w') as file:
                if st is not None:
                   file.write(st)
            print("Article has been written to " + str(count)+ ".txt")
    for i in range(bgn,23):
        links = getQuestionlinks('https://www.darmankade.com/blog/psychological-health/page/'+str(i)+'/')
        for link in links:
            st = get_article_text(link)
            count += 1
            with open(str(count)+ ".txt", 'w') as file:
                if st is not None:
                   file.write(st)
            print("Article has been written to " + str(count)+ ".txt")
    for i in range(bgn,83):
        links = getQuestionlinks('https://www.darmankade.com/blog/diseases/page/'+str(i)+'/')
        for link in links:
            st = get_article_text(link)
            count += 1
            with open(str(count)+ ".txt", 'w') as file:
                if st is not None:
                   file.write(st)
            print("Article has been written to " + str(count)+ ".txt")
    for i in range(bgn,17):
        links = getQuestionlinks('https://www.darmankade.com/blog/mother-and-child/page/'+str(i)+'/')
        for link in links:
            st = get_article_text(link)
            count += 1
            with open(str(count)+ ".txt", 'w') as file:
                if st is not None:
                   file.write(st)
            print("Article has been written to " + str(count)+ ".txt")
    for i in range(bgn,34):
        links = getQuestionlinks('https://www.darmankade.com/blog/health/page/'+str(i)+'/')
        for link in links:
            st = get_article_text(link)
            count += 1
            with open(str(count)+ ".txt", 'w') as file:
                if st is not None:
                   file.write(st)
            print("Article has been written to " + str(count)+ ".txt")
    for i in range(bgn,10):
        links = getQuestionlinks('https://www.darmankade.com/blog/medical-tests/page/'+str(i)+'/')
        for link in links:
            st = get_article_text(link)
            count += 1
            with open(str(count)+ ".txt", 'w') as file:
                if st is not None:
                   file.write(st)
            print("Article has been written to " + str(count)+ ".txt")

def get_article_text(url):
    html_content = getHTMLdocument(url)
    soup = BeautifulSoup(html_content, 'html.parser')
    article = soup.find('div', class_ = "entry-content")

    if article:
        return article.get_text(separator='\n', strip=True).split('آیا این مقاله برای شما مفید بود؟')[0]
    else:
        return None

if __name__ == '__main__':
    print(crawl_articles(0))