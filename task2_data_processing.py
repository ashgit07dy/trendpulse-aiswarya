import pandas as pd
import json
import os

# Step 1 — load JSON file

folder = "data"

files = os.listdir(folder)

# get latest json file
json_files = [f for f in files if f.endswith(".json")]
json_files.sort()

latest_file = json_files[-1]
file_path = os.path.join(folder, latest_file)

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

print(f"Loaded {len(df)} stories from {file_path}")


# Step 2 — Cleaning

# 1. removed duplicates
df = df.drop_duplicates(subset="post_id")
print("After removing duplicates:", len(df))


# 2. removed missing values
df = df.dropna(subset=["post_id", "title", "score"])
print("After removing nulls:", len(df))


# 3. fix data types
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)


# 4. removed low quality (score < 5)
df = df[df["score"] >= 5]
print("After removing low scores:", len(df))


# 5. removed extra spaces in title
df["title"] = df["title"].str.strip()


# Step 3 — save as CSV

csv_file = "data/trends_clean.csv"

df.to_csv(csv_file, index=False)

print(f"\nSaved {len(df)} rows to {csv_file}")


# Step 4 

print("\nStories per category:")
print(df["category"].value_counts())