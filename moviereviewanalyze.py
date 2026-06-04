import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "Age": [21, 22, None, 24, 25],
    "Marks": [80, 90, 85, None, 95]
}

df = pd.DataFrame(data)

# Cleaning
df.fillna(df.mean(), inplace=True)

print(df)

# Visualization
sns.scatterplot(x=df["Age"], y=df["Marks"])

plt.title("Age vs Marks")
plt.show()