# 🛡️ Hate Speech Detection System

An ML-powered web application designed to detect and classify toxic comments and hate speech in real-time. This project was developed as part of a Machine Learning university course.

## 🚀 Project Overview
The goal of this project is to create a safer online environment by automatically identifying toxic language.
The system uses **Natural Language Processing (NLP)** techniques to process text and a **Machine Learning model** (Logistic Regression / Random Forest) to classify it.

### Key Features:
* **Text Preprocessing:** Cleaning, tokenization, and stop-word removal.
* **TF-IDF Vectorization:** Converting text into numerical features.
* **Web Interface:** A user-friendly Flask web app for testing the model.
* **Real-time Prediction:** Instant classification of input text.

## 🛠️ Tech Stack
* **Language:** Python 3.12
* **Libraries:** `scikit-learn`, `pandas`, `flask`, `joblib`, `nltk`
* **Dataset:** Jigsaw Toxic Comment Classification Challenge

## 📂 Project Structure
```text
├── antrenare.py          # Script for training the ML model
├── aplicatia.py          # Flask web application
├── model_hate_speech.pkl # Saved trained model
├── vectorizer.pkl        # Saved TF-IDF vectorizer
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation
⚙️ Installation & Setup
Follow these steps to run the project locally:

1. Clone or Download the repository
Navigate to the project folder in your terminal.

2. Set up the Virtual Environment (Recommended)
# Create virtual environment
python3 -m venv venv

# Activate it (Linux/Mac)
source venv/bin/activate

# Activate it (Windows)
venv\Scripts\activate
3. Install Dependencies
Bash

pip install -r requirements.txt
4. Train the Model (First run only)
If the .pkl files are missing, train the model first:

Bash

python antrenare.py
5. Run the Application
Bash

python aplicatia.py
Open your browser and go to: http://127.0.0.1:5000
