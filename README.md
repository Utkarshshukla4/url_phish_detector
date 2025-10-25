## Contact

**Utkarsh Shukla**

Email- utqrshkumar07@gmail.com

GitHub- https://github.com/Utkarshshukla4

##  Overview
This project identifies malicious or phishing URLs by analyzing domain patterns, special characters, and length-based features.  
It can process single URLs or batches efficiently.

##  Features
- ML ensemble classifier  
- Detects phishing and suspicious URLs  
- Batch URL scanning  
- CLI interface  
- Cross-platform (Windows/Linux)

## Architecture:  

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


## Installation
git clone https://github.com/Utkarshshukla4/url_phish_detector.git

cd url_phish_detector


## Windows
python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt


## Linux / macOS
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt


## Running the Project
_Windows:_

python src\url_detector.py

_Linux / macOS:_

python3 src\url_detector.py


## Input Example
https://secure-login-update.freehoster.com

## Output Example
Prediction: Malicious URL
Confidence: 89%

## Summary

This detector identifies fake websites by analyzing URL structures, IPs, and domain patterns.
