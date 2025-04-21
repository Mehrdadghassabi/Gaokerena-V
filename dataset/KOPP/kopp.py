import fitz
import re
import pandas as pd



pdf_path = "پرسشنامه_علوم_پایه_دندان_پزشکی-اسفند1403.pdf"
year = "دندان اسفند 1403"


doc = fitz.open(pdf_path)
doc.delete_page(0)
doc.delete_page(-1)

text = ""
for page in doc:
    blocks = page.get_text("blocks")
    filtered_blocks = [
        block for block in blocks if block[1] > 50 and block[3] < page.rect.height - 30
    ]
    text += "\n".join([block[4] for block in filtered_blocks]) + "\n"

# with open("شهریور400.txt", "r", encoding="utf-8") as f:
#     text = f.read()


pattern = r"(?m)(?=^\d{1,3}[\s\n]*-[\n\s])"
splitted = re.split(pattern, text)
questions = [q.strip() for q in splitted if q.strip()]
with open("file_path", "w", encoding="utf-8") as f:
    for i, q in enumerate(questions, 1):
        f.write(f"{i}sssssssssssss{q}\n")

df = pd.DataFrame(columns=["Question", "Option1", "Option2", "Option3", "Option4", "Topic", "Source", "Correct answer"])

options_pattern = r"(\)\s*(الف|ب|ج|د)|(الف|ب|ج|د)\s*\))"
for i, question in enumerate(questions, 0):
    if i == 0 or i == 126 or i == 134 or i == 137:
        continue
    if i > 180:
        break
    q = question.replace("\n", "")
    splitted_options = re.findall(options_pattern, q)

    splitted = re.split(options_pattern, q)
    # if i > 0 and i < 37:
    #     topic = "فیزیولوژی"
    # elif i > 36 and i < 57:
    #     topic = "بیوشیمی"
    # elif i > 56 and i < 73:
    #     topic = "باکتری شناسی"
    # elif i > 72 and i < 83:
    #     topic = "انگل شناسی"
    # elif i > 82 and i < 86:
    #     topic = "حشره شناسی"
    # elif i > 85 and i < 90:
    #     topic = "قارچ شناسی"
    # elif i > 89 and i < 96:
    #     topic = "ویروس شناسی"
    # elif i > 95 and i < 150:
    #     topic = "تشریح"
    # else:
    #     topic = "اصول خدمات سلامت"
    topic = ""
    
    # if splitted[1] == "الف":
    if len(splitted) >= 8:
        df.loc[len(df)] = [splitted[0], splitted[4], splitted[8], splitted[12], splitted[16], topic, year, ""]
    else:
        df.loc[len(df)] = [splitted[0], splitted[2], splitted[4], splitted[6], "", topic, year, ""]
    # elif splitted[1] == "د":
    #     if len(splitted) >= 8:
    #         df.loc[len(df)] = [splitted[0], splitted[8], splitted[6], splitted[4], splitted[2], topic, year, ""]
    #     else:
    #         df.loc[len(df)] = [splitted[0], splitted[8], splitted[6], splitted[4], "", topic, year, ""]


df.to_excel(f"{year}.xlsx", index=False)
