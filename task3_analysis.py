import pandas as pd
import os

# Step 1 - load CSV
file_path = "data/cleaned_trends.csv"

if not os.path.exists(file_path):
    print("CSV file not found")
    exit()

df = pd.read_csv(file_path)

print("data loaded!")
print("total records:", len(df))


# Step 2 - basic analysis

# 1. count of posts per category
category_count = df["category"].value_counts()

print("\nPosts per category:")
print(category_count)


# 2. average score per category
avg_score = df.groupby("category")["score"].mean()

print("\nAverage score per category:")
print(avg_score)


# 3. most commented post
top_comments = df.sort_values(by="num_comments", ascending=False).head(1)

print("\nMost commented post:")
print(top_comments[["title", "num_comments"]])


# 4. top 5 highest scored posts
top_score = df.sort_values(by="score", ascending=False).head(5)

print("\nTop 5 posts by score:")
print(top_score[["title", "score"]])


# 5. most active author
top_author = df["author"].value_counts().head(1)

print("\nMost active author:")
print(top_author)