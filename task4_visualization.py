# Task 4 — Visualizations

import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------
# 1 — Setup
# -------------------------------

# loading the analysed data from task 3
df = pd.read_csv("data/trends_analysed.csv")

# checking if outputs folder is there, illa na create pannuren
if not os.path.exists("outputs"):
    os.makedirs("outputs")


# small helper function to cut long titles
def shorten_title(title):
    # romba perusa irundha cut pannuren for better display
    return title[:50] + "..." if len(title) > 50 else title


# -------------------------------
# 2 — Chart 1: Top 10 Stories
# -------------------------------

# score based ah sort panni top 10 eduthen
top_stories = df.sort_values(by="score", ascending=False).head(10)

titles = top_stories["title"].apply(shorten_title)
scores = top_stories["score"]

plt.figure()

# horizontal bar chart use pannuren
plt.barh(titles, scores)

plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")

# highest score top la varanum nu reverse pannuren
plt.gca().invert_yaxis()

# save pannuren
plt.savefig("outputs/chart1_top_stories.png")

plt.close()


# -------------------------------
# 3 — Chart 2: Stories per Category
# -------------------------------

# each category la evlo stories nu count pannuren
category_counts = df["category"].value_counts()

plt.figure()

# simple bar chart
plt.bar(category_counts.index, category_counts.values)

plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

# labels overlap aagatha nu rotate pannuren
plt.xticks(rotation=45)

plt.savefig("outputs/chart2_categories.png")

plt.close()


# -------------------------------
# 4 — Chart 3: Score vs Comments
# -------------------------------

plt.figure()

# popular and non-popular separate pannuren
popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

# scatter plot use pannuren relation paakanum nu
plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")

plt.legend()

plt.savefig("outputs/chart3_scatter.png")

plt.close()


# -------------------------------
# Bonus — Dashboard
# -------------------------------

# 3 charts ah onnu la combine pannuren
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# chart 1
axes[0].barh(titles, scores)
axes[0].set_title("Top Stories")
axes[0].invert_yaxis()

# chart 2
axes[1].bar(category_counts.index, category_counts.values)
axes[1].set_title("Categories")
axes[1].tick_params(axis='x', rotation=45)

# chart 3
axes[2].scatter(popular["score"], popular["num_comments"], label="Popular")
axes[2].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
axes[2].set_title("Score vs Comments")
axes[2].legend()

# overall title
plt.suptitle("TrendPulse Dashboard")

# save pannuren
plt.savefig("outputs/dashboard.png")

plt.close()


print("All charts saved in outputs folder")