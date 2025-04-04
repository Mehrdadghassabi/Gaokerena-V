<div align="center">
  <img src="https://github.com/user-attachments/assets/fa5782f3-bf6e-4ff1-987d-517e6f2d135f"/>
</div>

[![quick start](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Mehrdadghassabi/Gaokerena/blob/master/assets/Untitled4.ipynb)

---

## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [🌱 Our contribution](#-our-contribution)
- [🕵🏼‍♀️ Features](#-features)
- [📚 Base model](#-base-model)
- [🏃 Training process](#-training-process)
- [📊 Results](#-Results)
- [⛔️ License](#-Results)
- [⚠️ Risks and Limitations](#-risks-and-limitations)
- [🤝 Collaborators](#-collaborators)
- [🙏🏼 Acknowledgement](#-acknowledgement)

---

## 📍 Overview
Welcome to the Gaokerena Project! We’re excited to share an innovative initiative aimed at advancing natural language processing for the Persian-speaking medical community.\
Gaokerena is compact but powerful, designed to run smoothly even on home devices while keeping privacy and security—essential for medical use—at the forefront. We trained it on a new Persian medical dataset, including free-form Q&A, to make healthcare information more accessible and interactions safer.\
AI has huge potential to improve medicine, and with Gaokerena, we’re working to bring that potential to the Persian-speaking world.

## 🌱 Our contribution
- Introducing the first open source persian medical language model
- Introducing high quality Persian Medical resources including:

    1. [90M-token Persian medical corpus](https://huggingface.co/datasets/gaokerena/medical_corpus) (crawled from diverse sources).

    2. [MF3QA](https://github.com/Mehrdadghassabi/Gaokerena/tree/main/dataset/MF3QA): about 186k medical free form QA pairs(crawled from diverse sources) and 20k cleaned QA pairs.
 
    4. [Translation](https://github.com/Mehrdadghassabi/Gaokerena/tree/main/dataset/KQA_fa) of [K-QA](https://github.com/Itaymanes/K-QA/blob/main/dataset/questions_w_answers.jsonl) benchmark into persian

    6. [Translation](https://github.com/Mehrdadghassabi/Gaokerena/tree/main/dataset/MMLU_fa) of medical portion of [MMLU](https://github.com/Itaymanes/K-QA/blob/main/dataset/questions_w_answers.jsonl) benchmark into persian

## 🕵🏼‍♀️ Features
- First [Open-Source](https://huggingface.co/gaokerena/gaokerena-v1) Persian Medical Model: The only publicly available Persian language model fine-tuned specifically for medical applications. making it freely available for research and other applications.
- The first small language model to pass the Iranian Basic Medical Sciences Entrance Exam (کنکور علوم پایه پزشکی)

- Great Results: Stands out by delivering better results than other related models, including those that pair English medical models with translation systems. It excels at accurately interpreting medical questions and providing clear, reliable answers in Persian, making it highly effective for healthcare needs.

- Focus on Privacy and Ease: built upon a small language model it have local deployment capability, ensuring sensitive medical data remains secure and confidential.

## 📚 Base model
Gaokerena is built on [aya-expanse-8b](https://huggingface.co/CohereForAI/aya-expanse-8b), a robust and efficient language model selected for its proven performance and adaptability. This base model was fine-tuned to address the specific requirements of Persian medical applications, ensuring optimal accuracy and performance.

## 🏃 Training process
The Gaokerena model was trained through a  process that involved fine-tuning the Aya-ExPanse-8B base model on 60% of our Persian medical corpus, using the LoRA method for efficiency. This was followed by instruction tuning on our free-form question-answering dataset [MF3QA](https://huggingface.co/datasets/gaokerena/MF3QA), optimizing it for Persian medical queries.  The training was conducted on A100 PCIe 40/80G hardware via the Google Cloud Platform in the asia-east1 region, operating for 19 hours and resulting in a carbon footprint of 2.66 kg CO2 equivalent emissions.

## 📊 Results

## ⛔️ License
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) (non-commercial use only)

## ⚠️ Risks and Limitations
While Gaokerena aims to provide accurate information, it is not a substitute for professional medical advice. The model may have limitations in:

- Handling medical emergencies.
- Addressing highly specialized or rare medical conditions.
- Offering region-specific guidance, as the training data does not include localized Persian medical practices.

## 🤝 Collaborators
1. Mehrdad Ghassabi
2. Pedram Rostami
3. Amirhossein Poursina
4. Zahra Kazemi
5. Milad Tavakoli
## 🙏🏼 Acknowledgement
We would like to thank 
- Amir Jahani for his help with the data cleaning process.
- journeyfree.ai for creating logo.
- mohammad ghafghazian for crawling some part of data and putting it [here](https://www.kaggle.com/datasets/mohamadghafghaziyan/persian-medical-qa-dataset).
