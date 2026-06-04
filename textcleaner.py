import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

text = "This is a simple NLP text cleaning example."

tokens = word_tokenize(text)

filtered = [
    word for word in tokens
    if word.lower() not in stopwords.words('english')
]

print(filtered)