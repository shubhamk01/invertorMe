import requests

def fetch_stock_history(symbol, broker_api_url, api_key):
    """
    Fetch historical and current stock data from a broker API.
    :param symbol: Stock symbol.
    :param broker_api_url: Broker API endpoint.
    :param api_key: API key for authentication.
    :return: List of historical prices (date, price).
    """
    # Example for a generic broker API
    url = f"{broker_api_url}/stocks/{symbol}/history"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()  # Should return a list of {date, price}
    else:
        raise Exception("Failed to fetch stock data from broker.")
