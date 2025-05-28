import requests
import os
from datetime import datetime
from dotenv import load_dotenv

import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../.env'))
load_dotenv(dotenv_path)
NEWS_API_KEY = os.getenv("NEWSDATA_API_KEY")
print(f"Loaded API Key: {NEWS_API_KEY}")


def fetch_international_news(start_time: datetime, end_time: datetime, page_size=20):
    url = "https://newsdata.io/api/1/news"
    params = {
        "apikey": NEWS_API_KEY,
        "q": "global OR international OR UN",
        "language": "en",
        "country": "us,gb,fr,in",
    }

    print(f"Calling NewsData API with: {params}")
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"API Error: {response.text}")
        return []

    data = response.json()
    articles = data.get("results", [])

    return [article.get("title", "No Title") for article in articles]



