<div align="center">
  <img src="https://github.com/user-attachments/assets/fa5782f3-bf6e-4ff1-987d-517e6f2d135f"/>
</div>

<div align="center">
 [![quick start](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Mehrdadghassabi/Gracc/blob/master/Gracc.ipynb
</div>

# Overview
Welcome to the Gaokerena Project! We’re excited to share an innovative initiative aimed at advancing natural language processing for the Persian-speaking medical community.\
Gaokerena is compact but powerful, designed to run smoothly even on home devices while keeping privacy and security—essential for medical use—at the forefront. We trained it on a new Persian medical dataset, including free-form Q&A, to make healthcare information more accessible and interactions safer.\
AI has huge potential to improve medicine, and with Gaokerena, we’re working to bring that potential to the Persian-speaking world.

# Features
- First Open-Source Persian Medical Model: The only publicly available Persian language model fine-tuned specifically for medical applications. making it freely available for research and other applications.
- The first model to pass the Iranian Basic Medical Sciences Entrance Exam
- High-Quality Persian Medical resources introduced including:

    1. 90M-token Persian medical corpus (crawled from diverse sources).

    2. MF3QA: 20k filtered medical free form QA pairs (crawled from diverse sources).
 
    4. Translation of [K-QA](https://github.com/Itaymanes/K-QA/blob/main/dataset/questions_w_answers.jsonl) benchmark into persian

    6. Translation of medical portion of [MMLU](https://github.com/Itaymanes/K-QA/blob/main/dataset/questions_w_answers.jsonl) benchmark into persian

- Great Results: Stands out by delivering better results than other related models, including those that pair English medical models with translation systems. It excels at accurately interpreting medical questions and providing clear, reliable answers in Persian, making it highly effective for healthcare needs.

- Focus on Privacy and Ease: A lightweight model (based on aya-expanse-8b) optimized for local deployment, ensuring sensitive medical data remains secure and confidential.

# Dataset
A highlight of the Gaokerena project is the  dataset our team has developed—the first ever created for Persian medical language processing. We’ve built two essential resources that set a new standard for the field:
- Persian Medical Corpus: This is the first collection of its kind, built by gathering around 90 million tokens and 100,000 articles from various Persian medical websites and sources. It gives Gaokerena the foundation it needs to understand and generate accurate medical content in Persian. 
- Question-Answer Dataset: We also developed the first Persian dataset for medical question answering, collecting over 140,000 question-answer pairs from online forums. Our team tried hard to clean and filter this data, ensuring it’s high-quality and useful for training the model to handle real-world medical queries effectively.

Both datasets are fully open-source, inviting researchers and developers to build on our work and advance Persian medical NLP.

# Base model
Gaokerena is built on [aya-expanse-8b](https://huggingface.co/CohereForAI/aya-expanse-8b), a robust and efficient language model selected for its proven performance and adaptability. This base model was fine-tuned to address the specific requirements of Persian medical applications, ensuring optimal accuracy and performance.

# Training process
The Gaokerena model was trained through a  process that involved fine-tuning the Aya-ExPanse-8B base model on 60% of our Persian medical corpus, using the LoRA method for efficiency. This was followed by instruction tuning on our free-form question-answering dataset, optimizing it for Persian medical queries.  The training was conducted on A100 PCIe 40/80G hardware via the Google Cloud Platform in the asia-east1 region, operating for 19 hours and resulting in a carbon footprint of 2.66 kg CO2 equivalent emissions.
