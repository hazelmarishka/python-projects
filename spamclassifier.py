from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

messages = [
    "Win money now",
    "Hello how are you",
    "Claim your free prize",
    "Let's meet tomorrow"
]

labels = ["Spam", "Ham", "Spam", "Ham"]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

model = MultinomialNB()
model.fit(X, labels)

test = ["free money"]

prediction = model.predict(vectorizer.transform(test))

print(prediction[0])