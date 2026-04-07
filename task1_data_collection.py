import requests
import json
import os
import time
from datetime import datetime

# API urls
top_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
item_url = "https://hacker-news.firebaseio.com/v0/item/{}.json"

headers = {"User-Agent": "TrendPulse/1.0"}

# category keywords
category_keywords = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

# function to find category
def get_category(title):
    title = title.lower()
    for cat in category_keywords:
        for word in category_keywords[cat]:
            if word in title:
                return cat
    return None


# Step 1 - fetch top story ids
try:
    res = requests.get(top_url, headers=headers)
    ids = res.json()
    ids = ids[:1200]   # enough data for all categories
except:
    print("error fetching ids")
    ids = []


all_data = []

# Step 2 - category wise loop
for cat in category_keywords:

    print("collecting", cat, "...")

    count = 0

    for sid in ids:

        if count >= 25:
            break

        try:
            r = requests.get(item_url.format(sid), headers=headers)

            if r.status_code != 200:
                continue

            story = r.json()

            if not story or "title" not in story:
                continue

            title = story["title"]

            c = get_category(title)

            # fallback logic (imp fix)
            if not c:
                c = cat

            if c != cat:
                continue

            data = {
                "post_id": story.get("id"),
                "title": title,
                "category": c,
                "score": story.get("score", 0),
                "num_comments": story.get("descendants", 0),
                "author": story.get("by", "unknown"),
                "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            all_data.append(data)
            count += 1

        except:
            print("error in id:", sid)
            continue

    time.sleep(2)   # required delay


# Step 3 - save file

if not os.path.exists("data"):
    os.mkdir("data")

file_name = "data/trends_" + datetime.now().strftime("%Y%m%d") + ".json"

with open(file_name, "w", encoding="utf-8") as f:
    json.dump(all_data, f, indent=4)

print("done!")
print("total collected:", len(all_data))
print("file saved at:", file_name)