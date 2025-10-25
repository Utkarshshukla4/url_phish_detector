##  Overview
This project identifies malicious or phishing URLs by analyzing domain patterns, special characters, and length-based features.  
It can process single URLs or batches efficiently.

##  Features
- ML ensemble classifier  
- Detects phishing and suspicious URLs  
- Batch URL scanning  
- CLI interface  
- Cross-platform (Windows/Linux)

-  **Architecture Diagram:**   

[URL Input]
      ↓
[Feature Extraction (length, digits, symbols, domain age)]
      ↓
[Trained Classifier (Logistic Regression / Decision Tree)]
      ↓
[Prediction: Malicious / Safe]

## Project Structure

url-phish-detector/
├── src/
├── sample_data/
├── docs/
│   └── architecture.png
├── requirements.txt
├── README.md
└── .gitignore

## Steps

Clone this repository.

Create a virtual environment.

Install dependencies


## For First Installation
git clone https://github.com/Utkarshshukla4/email-phish-detector.git

cd email-phish-detector


## Windows
python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt


## Linux / macOS
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt


## Running the Project
Windows

python main.py

Linux / macOS

python3 main.py
