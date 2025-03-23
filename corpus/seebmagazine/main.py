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
    for div in soup.find_all('div',class_ = "grid_img"):
       for link in div.find_all('a',
                              attrs={'href': re.compile("^https://seebmagazine.com/")}):
           #if link.parent.name == 'article':
           links.add(link.get('href'))
    return links

def remove_nested_curly_braces(text):
    stack = []
    result = []
    i = 0
    substring_to_remove = """.IRPP_ruby , .IRPP_ruby .postImageUrl , .IRPP_ruby .centered-text-area  .IRPP_ruby , .IRPP_ruby:hover , .IRPP_ruby:visited , .IRPP_ruby:active  .IRPP_ruby .clearfix:after  .IRPP_ruby  .IRPP_ruby:active , .IRPP_ruby:hover  .IRPP_ruby .postImageUrl  .IRPP_ruby .centered-text-area  .IRPP_ruby .centered-text  .IRPP_ruby .IRPP_ruby-content  .IRPP_ruby .ctaText  .IRPP_ruby .postTitle  .IRPP_ruby .ctaButton  .IRPP_ruby .ctaButton  .IRPP_ruby:after"""
    while i < len(text):
        if text[i] == '{':
            stack.append(len(result))
        elif text[i] == '}':
            if stack:
                start_index = stack.pop()
                result = result[:start_index]
        else:
            if not stack:
                result.append(text[i])
        i += 1

    return ''.join(result).replace(substring_to_remove, '')

def get_article_text(url):
    html_content = getHTMLdocument(url)
    soup = BeautifulSoup(html_content, 'html.parser')
    article = soup.find('div', id = "cont_p")

    if article:
        return remove_nested_curly_braces(article.get_text(separator='\n', strip=True))
    else:
        return None

def crawl_articles(bgn,num_available_pages):
    count = 0
    for i in range(bgn,num_available_pages+1):
        links = getQuestionlinks('https://seebmagazine.com/category/medical-articles/page/'+str(i)+'/')
        for link in links:
            st = get_article_text(link)
            count += 1
            with open(str(count)+ ".txt", 'w') as file:
                if st is not None:
                   file.write(st)
            print("Article has been written to " + str(count)+ ".txt")

if __name__ == '__main__':
    crawl_articles(1, 39)