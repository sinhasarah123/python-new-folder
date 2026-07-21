import pandas as pd
import matplotlib.pyplot as plt

# 1. Import the dataset
df = pd.read_csv("IMDB-Movie-Data.csv")   # Replace with your actual file name

# 2. Print the first three and last three rows
print(df.head(3))
print(df.tail(3))

# 3. Check detailed information
print(df.info())

# 4. Check for null values
print(df.isnull().sum())

# 5. Create a subset of rows 41 to 75
subset = df.iloc[40:75]
print(subset)

# 6. Movie with the highest number of votes
highest_votes = df.loc[df["No_of_Votes"].idxmax()]
print(highest_votes)

# 7. Boxplot for IMDB_Rating and Runtime
df[["IMDB_Rating", "Runtime"]].boxplot()
plt.show()

# 8. Relationship between IMDB_Rating and Runtime
plt.scatter(df["Runtime"], df["IMDB_Rating"])
plt.xlabel("Runtime")
plt.ylabel("IMDB Rating")
plt.title("Runtime vs IMDB Rating")
plt.show()

# 9. Distribution of IMDB_Rating and Runtime
df["IMDB_Rating"].hist()
plt.title("Distribution of IMDB Rating")
plt.show()

df["Runtime"].hist()
plt.title("Distribution of Runtime")
plt.show()

# 10. Count plot of Certificate (Movie Rating)
df["Certificate"].value_counts().plot(kind="bar")
plt.title("Number of Movies by Certificate")
plt.xlabel("Certificate")
plt.ylabel("Count")
plt.show()