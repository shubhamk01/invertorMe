import requests
from app.services.analysis_service import analyze_sentiment

def fetch_and_analyze_news(keywords, api_key, max_articles=10):
    """
    Fetch news articles for given keywords and analyze their sentiment.
    :param keywords: List of keywords (e.g., stock symbols or company names).
    :param api_key: News API key.
    :param max_articles: Maximum number of articles to fetch per keyword.
    :return: List of dicts with article info and sentiment impact.
    """
    all_results = []
    for keyword in keywords:
        url = (
            f"https://newsapi.org/v2/everything?q={keyword}&pageSize={max_articles}&apiKey={api_key}"
        )
        response = requests.get(url)
        if response.status_code == 200:
            articles = response.json().get("articles", [])
            for article in articles:
                title = article.get("title", "")
                description = article.get("description", "")
                content = f"{title}. {description}"
                sentiment_score = analyze_sentiment(content)
                impact = "positive" if sentiment_score > 0.1 else "negative" if sentiment_score < -0.1 else "neutral"
                all_results.append({
                    "keyword": keyword,
                    "title": title,
                    "description": description,
                    "url": article.get("url"),
                    "sentiment_score": sentiment_score,
                    "impact": impact,
                })
    return all_results

def fetch_and_analyze_news(symbol, news_api_key, max_articles=10):
    """
    Fetch news for a stock and analyze sentiment.
    :param symbol: Stock symbol.
    :param news_api_key: News API key.
    :param max_articles: Number of articles to fetch.
    :return: List of dicts with article info and sentiment.
    """
    url = f"https://newsapi.org/v2/everything?q={symbol}&pageSize={max_articles}&apiKey={news_api_key}"
    response = requests.get(url)
    results = []
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        for article in articles:
            content = f"{article.get('title', '')}. {article.get('description', '')}"
            sentiment_score = analyze_sentiment(content)
            impact = "positive" if sentiment_score > 0.1 else "negative" if sentiment_score < -0.1 else "neutral"
            results.append({
                "title": article.get("title"),
                "description": article.get("description"),
                "url": article.get("url"),
                "sentiment_score": sentiment_score,
                "impact": impact,
            })
    return results