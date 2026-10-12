import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, classification_report

print("=" * 40)
print("       SPAM EMAIL CLASSIFIER")
print("=" * 40)

# Load dataset
data = pd.read_csv("dataset.csv")

print("\nDataset Loaded Successfully!")
print("Total Emails:", len(data))

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    data["text"],
    data["label"],
    test_size=0.25,
    random_state=42,
    stratify=data["label"]
)

# Create AI model
model = make_pipeline(
    TfidfVectorizer(),
    MultinomialNB()
)

# Train model
model.fit(X_train, y_train)

print("\nAI Model Trained Successfully!")

# Test model accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# Multiple email testing
print("\n" + "=" * 40)
print("       EMAIL TESTING")
print("=" * 40)

while True:
    text = input("\nEnter email (or exit): ")

    if text.lower() == "exit":
        print("Thank you for using our AI!")
        break

    prediction = model.predict([text])[0]

    if prediction == "spam":
        print("Result: SPAM EMAIL")
    else:
        print("Result: NOT SPAM")