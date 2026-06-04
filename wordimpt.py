from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

documents = [
    "AI is transforming technology",
    "Machine learning is part of AI"
]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(documents)

df = pd.DataFrame(
    X.toarray(),
    columns=vectorizer.get_feature_names_out()
)

print(df)