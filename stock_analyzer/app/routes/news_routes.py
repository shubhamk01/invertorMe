from fastapi import APIRouter

from stock_analyzer.app.models.news import search_news

router = APIRouter()

@router.get("/news")
def search_news_endpoint(query: str):
    return search_news(query)
