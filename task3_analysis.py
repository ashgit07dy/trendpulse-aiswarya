# Task 3 — Analysis with Pandas & NumPy

import pandas as pd
import numpy as np

# -------------------------------
# 1 — Load and Explore
# -------------------------------

# loading the cleaned csv file from previous task
df = pd.read_csv("data/trends_clean.csv")

# just checking how big the data is
print("Loaded data:", df.shape)

# seeing first few rows to understand data
print("\nFirst 5 rows:")
print(df.head())

# calculating average score and comments
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print("\nAverage score   :", round(avg_score, 2))
print("Average comments:", round(avg_comments, 2))


# -------------------------------
# 2 — Basic Analysis with NumPy
# -------------------------------

print("\n--- NumPy Stats ---")

# converting pandas columns to numpy arrays
scores = df["score"].to_numpy()
comments = df["num_comments"].to_numpy()

# basic stats using numpy
print("Mean score   :", round(np.mean(scores), 2))
print("Median score :", round(np.median(scores), 2))
print("Std deviation:", round(np.std(scores), 2))

# checking max and min values
print("Max score    :", np.max(scores))
print("Min score    :", np.min(scores))

# finding which category has more stories
category_counts = df["category"].value_counts()
top_category = category_counts.idxmax()
top_count = category_counts.max()

print(f"\nMost stories in: {top_category} ({top_count} stories)")

# finding which story got most comments
max_comments_index = np.argmax(comments)
top_story = df.iloc[max_comments_index]

print("\nMost commented story:")
print(f"\"{top_story['title']}\" — {top_story['num_comments']} comments")


# -------------------------------
# 3 — Add New Columns
# -------------------------------

# engagement means how much discussion per score
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# marking stories as popular if score is above average
df["is_popular"] = df["score"] > avg_score


# -------------------------------
# 4 — Save the Result
# -------------------------------

# saving the updated file for next task
output_path = "data/trends_analysed.csv"
df.to_csv(output_path, index=False)

print(f"\nSaved to {output_path}")