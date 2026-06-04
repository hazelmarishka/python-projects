from sklearn.neighbors import KNeighborsClassifier

# Height and Weight
X = [
    [150, 50],
    [160, 60],
    [170, 70],
    [180, 80]
]

# Labels
y = ["Small", "Medium", "Medium", "Large"]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

prediction = model.predict([[165, 65]])

print("Prediction:", prediction[0])