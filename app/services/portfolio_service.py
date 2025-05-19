from app.services.broker_service import fetch_stock_history
from app.services.news_service import fetch_and_analyze_news
from app.services.analysis_service import lstm_forecast, trading_signal

def auto_trade(symbols, amount, broker_api_url, broker_api_key, news_api_key):
    """
    Automatically trade stocks to target 10% monthly profit.
    :param symbols: List of stock symbols.
    :param amount: Available capital.
    :param broker_api_url: Broker API endpoint.
    :param broker_api_key: Broker API key.
    :param news_api_key: News API key.
    :return: Trade actions and updated portfolio.
    """
    portfolio = {}
    for symbol in symbols:
        history = fetch_stock_history(symbol, broker_api_url, broker_api_key)
        prices = [entry['price'] for entry in history]
        current_price = prices[-1]
        predicted_price = lstm_forecast(prices)
        news = fetch_and_analyze_news(symbol, news_api_key)
        # Use the most recent news impact
        if news:
            news_impact = news[0]['impact']
        else:
            news_impact = "neutral"
        action = trading_signal(predicted_price, current_price, news_impact)
        portfolio[symbol] = {
            "current_price": current_price,
            "predicted_price": predicted_price,
            "news_impact": news_impact,
            "action": action
        }
        # Here, you would add logic to execute the trade via broker API
        # and update the amount/portfolio accordingly.
    # Add logic to check if 10% profit is achieved and adjust strategy.
    return portfolio