import pandas as pd
import matplotlib.pyplot as plt
import os

# Step 1 - load CSV
file_path = "data/cleaned_trends.csv"

if not os.path.exists(file_path):
    print("CSV file not found")
    exit()

df = pd.read_csv(file_path)

print("data loaded!")

# Step 2 - category count graph

category_count = df["category"].value_counts()

plt.figure()
category_count.plot(kind="bar")
plt.title("Number of Posts per Category")
plt.xlabel("Category")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()


# Step 3 - average score graph

avg_score = df.groupby("category")["score"].mean()

plt.figure()
avg_score.plot(kind="bar")
plt.title("Average Score per Category")
plt.xlabel("Category")
plt.ylabel("Average Score")
plt.xticks(rotation=45)
plt.show()


# Step 4 - comments distribution

plt.figure()
plt.hist(df["num_comments"])
plt.title("Comments Distribution")
plt.xlabel("Number of Comments")
plt.ylabel("Frequency")
plt.show()