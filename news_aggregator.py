"""
Uses the News API to fetch the top headlines from a specific country and category.
"""

import json
import os

import requests

if __name__ == "__main__":
    country = "in"
    category = "business"
    api_key = os.environ.get("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={api_key}"

    response = requests.get(url)
    data = response.json()
    json.dump(data, open("news.json", "w"), indent=4)
