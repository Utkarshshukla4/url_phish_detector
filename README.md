# PhishGuard - Email + URL Phishing Detection

Simple combined tool that trains two small models:
- Email classifier (Logistic Regression on bag-of-words)
- URL classifier (RandomForest on URL features)

How to run:
1. Create & activate venv
2. pip install -r requirements.txt
3. python src/train_email_model.py
4. python src/train_url_model.py
5. python src/phishguard.py
