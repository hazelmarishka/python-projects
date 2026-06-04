import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "Area": [1000, 1500, 2000, 2500, 3000],
    "Price": [20, 30, 40, 50, 60]
}

df = pd.DataFrame(data)

X = df[["Area"]]
y = df["Price"]

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[2200]])

print("Predicted Price:", prediction[0])

# Graph
plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.xlabel("Area")
plt.ylabel("Price")
plt.show()
