from bs4 import BeautifulSoup
import requests
import re
import sys

def getHTMLdocument(url):
    response = requests.get(url)
    return response.text

def getQuestionlinks(url_to_scrape):
    html_document = getHTMLdocument(url_to_scrape)
    soup = BeautifulSoup(html_document, 'html.parser')
    links = set()
    for link in soup.find_all('a',
                              attrs={'href': re.compile("^https://niniban.com/")}):
        if link.parent.name == 'h3':
           links.add(link.get('href'))
    return links

def get_article_text(url):
    html_content = getHTMLdocument(url)
    soup = BeautifulSoup(html_content, 'html.parser')
    article = soup.find('div', id = "echo_detail")
    if article:
        return article.get_text(separator='\n', strip=True)
    else:
        return None

def crawl_articles(bgn,num_available_pages):
    count = 0
    for i in range(bgn,num_available_pages+1):
        # get address from names
        addresses = [
            'https://niniban.com/بخش-آمادگی-بارداری-161',
            'https://niniban.com/بخش-قصد-با-وضعیت-خاص-164',
            'https://niniban.com/بخش-تعیین-جنسیت-56',
            'https://niniban.com/بخش-رابطه-با-همسر-163',
            'https://niniban.com/بخش-سلامت-زنان-117',
            'https://niniban.com/بخش-سلامت-مردان-165',
            'https://niniban.com/بخش-درمان-ناباروری-169',
            'https://niniban.com/بخش-ناباروری-زنان-166',
            'https://niniban.com/بخش-ناباروری-مردان-167',
            'https://niniban.com/بخش-روشهای-جایگزین-172',
            'https://niniban.com/بخش-علائم-بارداری-59',
            'https://niniban.com/بخش-آزمایشگاه-سونوگرافی-196',
            'https://niniban.com/بخش-تدارک-قبل-از-تولد-178',
            'https://niniban.com/بخش-بارداری-سه-ماهه-اول-173',
            'https://niniban.com/بخش-بارداری-سه-ماهه-دوم-174',
            'https://niniban.com/بخش-بارداری-سه-ماهه-سوم-175',
            'https://niniban.com/بخش-مراقبتهای-بارداری-142',
            'https://niniban.com/بخش-بارداری-خاص-177',
            'https://niniban.com/بخش-علائم-زایمان-76',
            'https://niniban.com/بخش-متخصص-زنان-زایمان-192',
            'https://niniban.com/بخش-آمادگی-برای-زایمان-83',
            'https://niniban.com/بخش-زایمان-طبیعی-77',
            'https://niniban.com/بخش-زایمان-سزارین-80',
            'https://niniban.com/بخش-زایمان-چندقلویی-180',
            'https://niniban.com/بخش-زایمان-زودرس-دیررس-79',
            'https://niniban.com/بخش-بعد-از-زایمان-152',
            'https://niniban.com/بخش-سلامت-نوزاد-181',
            'https://niniban.com/بخش-مراقبت-از-نوزاد-94',
            'https://niniban.com/بخش-تغذیه-شیردهی-نوزاد-90',
            'https://niniban.com/بخش-نوزاد-سبک-زندگی-183',
            'https://niniban.com/بخش-روانشناسی-نوزاد-182',
            'https://niniban.com/بخش-رشد-مراقبت-کودک-184',
            'https://niniban.com/بخش-متخصص-اطفال-205'
        ]
        for address in addresses:
           links = getQuestionlinks(address+'?page='+str(i))
           try:
              for link in links:
               st = get_article_text(link)
               count += 1
               if not 'سوال مخاطب نی‌نی‌بان' in st:
                  with open('./articles/'+str(count)+ ".txt", 'w') as file:
                       if st is not None:
                          file.write(st)
               elif sys.getsizeof(st) > 2000:
                  with open('./questions-articles/' + str(count) + ".txt", 'w') as file:
                       if st is not None:
                          file.write(st)
               else:
                   with open('./questions/' + str(count) + ".txt", 'w') as file:
                       if st is not None:
                           file.write(st)
               print("Article has been written to " + str(count)+ ".txt")
           except:
              print('some error has occurred')

if __name__ == '__main__':
    crawl_articles(1, 80)
