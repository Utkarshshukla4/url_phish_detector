import os
import re
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def extract_features(url):
    features = {}
    features["url_length"] = len(url)
    features["num_dots"] = url.count('.')
    features["num_hyphens"] = url.count('-')
    features["has_https"] = 1 if url.lower().startswith("https") else 0
    features["num_digits"] = sum(c.isdigit() for c in url)
    features["contains_ip"] = 1 if re.search(r"(\d{1,3}\.){3}\d{1,3}", url) else 0
    features["num_special_chars"] = len(re.findall(r"[?|@|=|&|_|!|~|$|#]", url))
    return features

data_path = os.path.join("data", "sample_urls.csv")
data = pd.read_csv(data_path)

feature_list = [extract_features(u) for u in data["url"]]
features_df = pd.DataFrame(feature_list)
labels = data["label"]

X_train, X_test, y_train, y_test = train_test_split(features_df, labels, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print(f"✅ URL model trained with accuracy: {accuracy*100:.2f}%")

os.makedirs("src", exist_ok=True)
joblib.dump(model, os.path.join("src", "url_model.pkl"))
print("💾 Saved url_model.pkl to src/")
