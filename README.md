<div align="center">
  <img src="https://github.com/user-attachments/assets/fa5782f3-bf6e-4ff1-987d-517e6f2d135f"/>
</div>
<p align="center">
📃 <a href="" target="_blank">Paper</a> ｜🤗 <a href="https://huggingface.co/gaokerena" target="_blank">huggingface repository</a> | 🚀 <a href="https://colab.research.google.com/github/Mehrdadghassabi/Gaokerena/blob/master/assets/Untitled4.ipynb" target="_blank">quick start</a>
</p>

## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [🌱 Our contribution](#-our-contribution)
- [🕵🏼‍♀️ Features](#-features)
- [📚 Base model](#-base-model)
- [🏃 Training process](#-training-process)
- [📊 Results](#-Results)
- [⚠️ Risks and Limitations](#-risks-and-limitations)
- [⛔️ License](#-Results)
- [🤝 Collaborators](#-collaborators)
- [🙏🏼 Acknowledgement](#-acknowledgement)

---

## 📍 Overview
Welcome to the Gaokerena Project! We’re excited to share an innovative initiative aimed at advancing natural language processing for the Persian-speaking medical community.\
Gaokerena is designed to run even on home devices while keeping privacy and security—essential for medical use—at the forefront. We trained it on a new Persian medical dataset, including free-form Q&A, to make healthcare information more accessible and interactions safer.\
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
- The first small(sub 8 billion parameters) language model to pass the Iranian Basic Medical Sciences Entrance Exam in real world condition (کنکور علوم پایه پزشکی)

- Great Results: Stands out by delivering better results than other related models, including those that pair English medical models with translation systems. It excels at accurately interpreting medical questions and providing clear, reliable answers in Persian, making it highly effective for healthcare needs.

- Focus on Privacy and Ease: built upon a small language model it have local deployment capability, ensuring sensitive medical data remains secure and confidential.

## 📚 Base model
Gaokerena is built on [aya-expanse-8b](https://huggingface.co/CohereForAI/aya-expanse-8b), a robust and efficient language model selected for its proven performance and adaptability. This base model was fine-tuned to address the specific requirements of Persian medical applications, ensuring optimal accuracy and performance.

## 🏃 Training process
The Gaokerena model was trained through a  process that involved fine-tuning the Aya-ExPanse-8B base model on 60% of our Persian medical corpus, using the LoRA method for efficiency. This was followed by instruction tuning on our free-form question-answering dataset [MF3QA](https://huggingface.co/datasets/gaokerena/MF3QA), optimizing it for Persian medical queries.  The training was conducted on A100 PCIe 40G hardware via the Google Cloud Platform in the asia-east1 region, operating for 19 hours and resulting in a carbon footprint of 2.66 kg CO2 equivalent emissions.

## 📊 Results
We have fully published the results [here](https://github.com/Mehrdadghassabi/Gaokerena/tree/main/evaluation). our model correctly answered about half of the questions in the medical portion of the MMLU dataset
and successfully passed Iranian Basic Medical Sciences Entrance Exam - Sept 2017 (کنکور علوم پایه پزشکی شهریور ۱۴۰۲) while other alternatives failed to.
### multiple choice qa
here it is the result against pipeline alternatives:
|                       | Gaokerena (ours)  | MedMobile + gemma2b-it | MedMobile + parsinlu |
|-----------------------|--------------------|----------------------------|------------------------|
| **MMLU-anatomy(fa)**  | **48.14**          | 14.07                      |   25.18                |
| **MMLU-medicalgenetics(fa)** | **53.0**    | 20.0                       | 35.0                   |
| **MMLU-collegemedicine(fa)** | **43.93**   | 19.08                      | 27.17                  |
| **MMLU-clinicalknowledge(fa)**     | **55.47**                        | 27.54                 | 31.70               |
| **MMLU-professionalmedicine(fa)**  | **47.05**                    | 17.27                  | 33.82               |
| **MMLU-collegebiology(fa)**      | **47.22**                        | 18.75                  | 31.25                |
| **MMLU(avg)**         | **49.31**                             | 20.11                  | 30.99                |
| **IBMSEE Sept 2023**  | **38.69**                              | 24.40                | 32.73                |

here it is the result against general purpose language models:
|                       | Gaokerena (ours) | aya_expanse8b (baseline) | Qwen2.5 | PersianMind |
|-----------------------|--------------------|---------------------------|---------|-------------|
| **MMLU-anatomy(fa)**  | **48.14**          | 40.74                     | 41.48   | 25.18       |
| **MMLU-medicalgenetics(fa)**      | **53.0**           | 49.0                      | 52.0    | 34.0        |
| **MMLU-collegemedicine(fa)**      | 43.93              | **44.51**                 | 43.35   | 20.23       |
| **MMLU-clinicalknowledge(fa)**     | **55.47**          | 52.07                     | 47.92   | 25.28       |
| **MMLU-professionalmedicine(fa)**  | **47.05**          | 45.58                     | 43.01   | 23.89       |          |
| **MMLU-collegebiology(fa)**      | **47.22**          | 45.14                     | 44.85   | 32.63       |
| **MMLU(avg)**         | **49.31**          | 46.64                     | 45.17   | 25.89       |
| **IBMSEE Sept 2023**   | **38.69**          | 34.52                     | 33.33   | 19.64       |
### free form choice qa
win rate against pipeline alternatives:

![image](https://github.com/user-attachments/assets/6de1498f-e5d1-459c-aa12-66a468aea98f)


win rate against general purpose language models:

![fig4](https://github.com/user-attachments/assets/aac5de66-3c51-4436-8d42-5eb52252c762)


## ⚠️ Risks and Limitations
While Gaokerena aims to provide relatively accurate information, it is not a substitute for professional medical advice. The model may have limitations in:

- Handling medical emergencies.
- Addressing highly specialized or rare medical conditions.
- Offering region-specific guidance, as the training data does not include localized Persian medical practices.

## ⛔️ License
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) (non-commercial use only)

## 🤝 Collaborators
1. Mehrdad Ghassabi
2. Pedram Rostami
3. Dr. Hamid Reza Baradaran Kashani
4. Amirhossein Poursina
5. Zahra Kazemi
6. Milad Tavakoli
## 🙏🏼 Acknowledgement
We would like to thank 
- Amir Jahani for his help with the data cleaning process.
- journeyfree.ai for creating logo.
- mohammad ghafghazian for crawling small portion of [dryab site](https://doctor-yab.ir) putting it [here](https://www.kaggle.com/datasets/mohamadghafghaziyan/persian-medical-qa-dataset), we used his data in MF3QA.
