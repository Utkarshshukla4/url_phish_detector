import os
import re
import joblib
import pandas as pd

def extract_url_features(url):
    features = {}
    features["url_length"] = len(url)
    features["num_dots"] = url.count('.')
    features["num_hyphens"] = url.count('-')
    features["has_https"] = 1 if url.lower().startswith("https") else 0
    features["num_digits"] = sum(c.isdigit() for c in url)
    features["contains_ip"] = 1 if re.search(r"(\d{1,3}\.){3}\d{1,3}", url) else 0
    features["num_special_chars"] = len(re.findall(r"[?|@|=|&|_|!|~|$|#]", url))
    return features

def run_email_check():
    # load email model & vectorizer
    model = joblib.load(os.path.join("src", "email_model.pkl"))
    vectorizer = joblib.load(os.path.join("src", "email_vectorizer.pkl"))
    email_text = input("\n📧 Paste the email text (single line or multiple lines):\n")
    features = vectorizer.transform([email_text])
    prediction = model.predict(features)[0]
    print("\nResult:", "⚠️ PHISHING" if prediction == "phishing" else "✅ Legitimate")

def run_url_check():
    model = joblib.load(os.path.join("src", "url_model.pkl"))
    url = input("\n🔗 Enter the URL to check:\n").strip()
    features = pd.DataFrame([extract_url_features(url)])
    prediction = model.predict(features)[0]
    print("\nResult:", "⚠️ PHISHING" if prediction == "phishing" else "✅ Legitimate")

def main():
    print("🛡️ PhishGuard — Email + URL Detection")
    print("Choose an option:")
    print("1 — Check Email")
    print("2 — Check URL")
    choice = input("Enter 1 or 2: ").strip()
    if choice == "1":
        run_email_check()
    elif choice == "2":
        run_url_check()
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
