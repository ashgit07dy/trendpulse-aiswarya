import json
import os
import pandas as pd

# Step 1 - find latest JSON file
folder = "data"

files = os.listdir(folder)

# get json files only
json_files = [f for f in files if f.endswith(".json")]

# take latest file
json_files.sort()
latest_file = json_files[-1]

file_path = os.path.join(folder, latest_file)

print("loading file:", latest_file)

# Step 2 - load json
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# convert to dataframe
df = pd.DataFrame(data)

print("total records:", len(df))

# Step 3 - cleaning

# remove duplicates based on post_id
df = df.drop_duplicates(subset="post_id")

# fill missing values
df["author"] = df["author"].fillna("unknown")
df["num_comments"] = df["num_comments"].fillna(0)

# optional: remove rows with no title
df = df[df["title"].notna()]

# Step 4 - save to csv

# create data folder if not exists
if not os.path.exists("data"):
    os.mkdir("data")

csv_file = "data/cleaned_trends.csv"

df.to_csv(csv_file, index=False)

print("cleaning done!")
print("saved file:", csv_file)