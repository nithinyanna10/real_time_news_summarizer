from fastapi import FastAPI, Request
from pydantic import BaseModel
from datetime import datetime
from typing import List

from .summarizer import summarize_articles
from .news_fetcher import fetch_international_news


app = FastAPI()

class SummaryRequest(BaseModel):
    start_time: datetime
    end_time: datetime

@app.post("/summarize")
async def summarize_news(request: SummaryRequest):
    articles = fetch_international_news(request.start_time, request.end_time)
    
    if not articles:
        return {"message": "No articles found during this time range."}

    summaries = summarize_articles(articles)
    return {"summaries": summaries}
