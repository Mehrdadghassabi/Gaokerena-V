from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import os
# install bs4,requests,pandas,openpyxl

def getHTMLdocument(url):
    response = requests.get(url)
    return response.text

def getQuestionlinks(url_to_scrape):
    html_document = getHTMLdocument(url_to_scrape)
    soup = BeautifulSoup(html_document, 'html.parser')
    links = []
    for link in soup.find_all('a',
                              attrs={'href': re.compile("^/faq/")}):
        links.append('https://doctor-yab.ir'+link.get('href'))
    links = links[0:len(links) - 7]
    return links

def get_question(link):
    req = requests.get(link)
    html_content = req.content.decode('utf-8')
    soup = BeautifulSoup(html_content, 'html.parser')
    h3_tag = soup.find('div',itemprop="text", class_="col-xs-12 faq-text")
    if h3_tag:
        return h3_tag.getText()
    else:
        return "Tag not found."

def get_answer(link):
    req = requests.get(link)
    html_content = req.content.decode('utf-8')
    soup = BeautifulSoup(html_content, 'html.parser')
    span = soup.find('p', class_="alert-warning2" , itemprop="text")
    if span:
        return span.getText()
    else:
        return ""

def save_qas(url_to_scrape,file_name):
    #url_to_scrape = "https://drhast.com/q/page-5"
    links = getQuestionlinks(url_to_scrape)
    data = {
        'Question': [
        ],
        'Answer': [
        ]
    }
    count = 0
    for link in links:
        data['Question'].append(get_question(link).strip())
        data['Answer'].append(get_answer(link).strip())
        count += 1

    df = pd.DataFrame(data)
    df.to_excel(file_name, index=False)
    print(f"Data written to {file_name} successfully.")

def merge_excel_files(folder_path):
    all_data = []
    for file in os.listdir(folder_path):
        if file.endswith('.xlsx'):
            file_path = os.path.join(folder_path, file)
            df = pd.read_excel(file_path)
            all_data.append(df)

    merged_df = pd.concat(all_data, ignore_index=True)
    merged_df = merged_df.drop_duplicates(subset=['Question'], keep='first')
    merged_file_path = os.path.join(folder_path, 'merged_file.xlsx')
    merged_df.to_excel(merged_file_path, index=False)

def crawl_qas(bgn):
    i = 1
    for p in range(1, 5101):
        if p <= bgn:
            continue
        try:
            url_to_scrape = "https://doctor-yab.ir/faq/?page=" + str(p)
            file_name = str(i) + '.xlsx'
            save_qas(url_to_scrape, file_name)
            print('page ' + str(p) + ' has been written.')
            i = i + 1
        except Exception as e:
            print(e)
    folder_path = './'
    merge_excel_files(folder_path)

def append_record_to_excel(file_path, Question,Answer):
    new_record = {
        'Question': Question,
        'Answer': Answer
    }
    new_record_df = pd.DataFrame([new_record])
    try:
        existing_df = pd.read_excel(file_path)
        updated_df = pd.concat([existing_df, new_record_df], ignore_index=True)
    except FileNotFoundError:
        updated_df = new_record_df

    updated_df.to_excel(file_path, index=False)

def isNaN(n):
    return n != n

def clean(in_path,out_path):
    df = pd.read_excel(in_path)
    for index, row in df.iterrows():
        print(index)
        Question = row['Question']
        Answer = row['Answer']
        if Question != 'Tag not found.' and Answer != 'Tag not found.' and not isNaN(Question) and not isNaN(Answer):
            append_record_to_excel(out_path, Question, Answer)

crawl_qas(2127)
