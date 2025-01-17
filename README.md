# EthioMart-NER-Named-Entity-Recognition-

Overview

EthioMart-NER is a project aimed at enhancing e-commerce activities in Ethiopia by leveraging Named Entity Recognition (NER) techniques on Amharic text. This repository contains the code and resources for extracting key business entities such as product names, prices, and locations from messages shared across various Ethiopian-based Telegram e-commerce channels.

Project Goals

- Real-time Data Extraction: Collect and process data from multiple Telegram channels to provide a unified shopping experience.

- Entity Recognition: Fine-tune Large Language Models (LLMs) to accurately identify and extract entities from Amharic text.

- Model Evaluation: Compare the performance of different NER models using metrics like precision, recall, and F1-score.

Key Features

- Data ingestion system for real-time message collection from Telegram.

- Preprocessing pipeline tailored for Amharic text, including tokenization and normalization.

- CoNLL format labeling for NER tasks.

- Fine-tuning of state-of-the-art LLMs for improved entity recognition.

- Model interpretability using SHAP and LIME for understanding model predictions.

Getting Started

Prerequisites

- Python 3.x

- Required libraries (see requirements.txt)

Installation

1. Clone the repository:

git clone https://github.com/Elelanfik/EthioMart-NER-Named-Entity-Recognition-.git

cd EthioMart-NER

2. Install the required packages:

pip install -r requirements.txt

Usage

1. Data Collection: Set up the data ingestion system to fetch messages from selected Telegram channels.

2. Preprocessing: Run the preprocessing script to clean and structure the data.

3. Labeling: Use the provided scripts to label the dataset in CoNLL format.

4. Model Training: Fine-tune the selected LLMs using the labeled dataset.

5. Evaluation: Evaluate model performance and interpret results using SHAP and LIME.

Example Commands

python data_collection.py
python preprocess.py
python label_data.py
python train_model.py
python evaluate_model.py

Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.

2. Create a new branch (git checkout -b feature/YourFeature).

3. Make your changes and commit them (git commit -m 'Add some feature').

4. Push to the branch (git push origin feature/YourFeature).

5. Open a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments

- Special thanks to the contributors and the community for their support.

- References to relevant literature and resources can be found in the documentation.

Contact

For any inquiries or feedback, please reach out to [fikadutsion@gmail.com].
