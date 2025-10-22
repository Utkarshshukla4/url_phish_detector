# email_detector.py

import joblib

# Load trained email model and vectorizer
model = joblib.load("src/email_model.pkl")
vectorizer = joblib.load("src/email_vectorizer.pkl")

print("📧 Email Phish Detector is ready!\n")

while True:
    email_text = input("Enter email text (or type 'exit' to quit): ")

    if email_text.lower() == "exit":
        print("Exiting Email Detector. Goodbye! 👋")
        break

    # Transform and predict
    features = vectorizer.transform([email_text])
    prediction = model.predict(features)[0]

    if prediction == "phishing":
        print("⚠️  This looks like a PHISHING email!\n")
    else:
        print("✅  This email seems legitimate.\n")
