from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import os

def getHTMLdocument(url):
    response = requests.get(url)
    return response.text

def getQuestionlinks(url_to_scrape):
    html_document = getHTMLdocument(url_to_scrape)
    soup = BeautifulSoup(html_document, 'html.parser')
    links = []
    for link in soup.find_all('a',
                              attrs={'href': re.compile("^https://drhast.com/q/")}):
        links.append(link.get('href'))
    links = links[0:len(links) - 1]
    return links

def get_question(link):
    req = requests.get(link)
    html_content = req.content.decode('utf-8')
    soup = BeautifulSoup(html_content, 'html.parser')
    h2_tag = soup.find('h2', class_='main-question__body', itemprop='text')
    if h2_tag:
        return h2_tag.getText()
    else:
        return "Tag not found."

def get_answer(link):
    req = requests.get(link)
    html_content = req.content.decode('utf-8')
    soup = BeautifulSoup(html_content, 'html.parser')
    span = soup.find('span', itemprop='text')
    if span:
        return span.getText()
    else:
        return "Tag not found."

def save_qas(url_to_scrape,file_name):
    #url_to_scrape = "https://drhast.com/q/page-5"
    links = getQuestionlinks(url_to_scrape)
    data = {
        'Question': [
        ],
        'Answer': [
        ]
    }
    for link in links:
        data['Question'].append(get_question(link))
        data['Answer'].append(get_answer(link))
    df = pd.DataFrame(data)
    df.to_excel(file_name, index=False)
    print(f"Data written to {file_name} successfully.")

def merge_excel_files(folder_path):
    all_data = []
    # Loop through all files in the specified folder
    for file in os.listdir(folder_path):
        if file.endswith('.xlsx'):
            file_path = os.path.join(folder_path, file)
            # Read the Excel file
            df = pd.read_excel(file_path)
            all_data.append(df)

    # Concatenate all dataframes into one
    merged_df = pd.concat(all_data, ignore_index=True)

    # Drop duplicate questions, keeping the first occurrence
    merged_df = merged_df.drop_duplicates(subset=['Question'], keep='first')

    # Save the merged file to a new Excel file
    merged_file_path = os.path.join(folder_path, 'merged_file.xlsx')
    merged_df.to_excel(merged_file_path, index=False)

def crawl_all_qas():
    i = 1
    for p in range(1, 21):
        try:
            url_to_scrape = "https://drhast.com/q/page-" + str(p)
            links = getQuestionlinks(url_to_scrape)
            for link in links:
                try:
                    file_name = str(i) + '.xlsx'
                    save_qas(link, file_name)
                    i = i + 1
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
    folder_path = './'
    merge_excel_files(folder_path)

def crawl_recent_qas():
    i = 1
    for p in range(1, 21):
        try:
            url_to_scrape = "https://drhast.com/q/page-" + str(p)
            file_name = str(i) + '.xlsx'
            save_qas(url_to_scrape, file_name)
            i = i + 1
        except Exception as e:
            print(e)
    folder_path = './'
    merge_excel_files(folder_path)

crawl_recent_qas()
