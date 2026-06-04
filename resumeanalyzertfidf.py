from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

resume = """
Python machine learning data analysis pandas numpy
"""

job_description = """
Looking for python and machine learning skills
"""

documents = [resume, job_description]

vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(documents)

score = cosine_similarity(tfidf[0:1], tfidf[1:2])

print("Resume Match Score:", score[0][0] * 100)