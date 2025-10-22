import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

data_path = os.path.join("data", "sample_emails.csv")
data = pd.read_csv(data_path)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['email_text'])
y = data['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print(f"✅ Email model trained with accuracy: {accuracy*100:.2f}%")

# Save model and vectorizer
os.makedirs("src", exist_ok=True)
joblib.dump(model, os.path.join("src", "email_model.pkl"))
joblib.dump(vectorizer, os.path.join("src", "email_vectorizer.pkl"))
print("💾 Saved email_model.pkl and email_vectorizer.pkl to src/")
