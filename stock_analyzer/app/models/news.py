from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

def index_news(news_data):
    """
    Index news into Elasticsearch.
    :param news_data: Dictionary containing the news data.
    """
    es.index(index="news", body=news_data)

def search_news(query):
    """
    Search news articles based on a query.
    :param query: Query string for Elasticsearch search.
    :return: Search results.
    """
    return es.search(index="news", body={"query": {"match": {"content": query}}})
