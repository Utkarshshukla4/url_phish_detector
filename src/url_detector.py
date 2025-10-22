# url_detector.py

import joblib

# Load trained URL model
model = joblib.load("src/url_model.pkl")

print("🌐 URL Phish Detector is ready!\n")

while True:
    url = input("Enter a URL (or type 'exit' to quit): ")

    if url.lower() == "exit":
        print("Exiting URL Detector. Goodbye! 👋")
        break

    # Predict phishing or safe
    prediction = model.predict([[url]])[0]

    if prediction == "phishing":
        print("⚠️  This looks like a PHISHING URL!\n")
    else:
        print("✅  This URL seems safe.\n")
