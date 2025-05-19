import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def lstm_forecast(prices, look_back=10, epochs=10):
    """
    Forecast future prices using LSTM.
    :param prices: List or np.array of historical prices.
    :param look_back: Number of time steps to look back.
    :param epochs: Training epochs.
    :return: Predicted next price.
    """
    scaler = MinMaxScaler(feature_range=(0, 1))
    prices = np.array(prices).reshape(-1, 1)
    scaled_prices = scaler.fit_transform(prices)

    X, y = [], []
    for i in range(len(scaled_prices) - look_back):
        X.append(scaled_prices[i:i+look_back, 0])
        y.append(scaled_prices[i+look_back, 0])
    X, y = np.array(X), np.array(y)
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))

    model = Sequential()
    model.add(LSTM(50, input_shape=(look_back, 1)))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(X, y, epochs=epochs, batch_size=1, verbose=0)

    last_sequence = scaled_prices[-look_back:].reshape(1, look_back, 1)
    next_price_scaled = model.predict(last_sequence)
    next_price = scaler.inverse_transform(next_price_scaled)[0][0]
    return float(next_price)

def analyze_sentiment(text):
    """
    Analyze sentiment of news text using NLTK's VADER.
    :param text: News article or headline.
    :return: Sentiment score (-1 to 1).
    """
    nltk.download('vader_lexicon', quiet=True)
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    return sentiment['compound']

def trading_signal(predicted_price, current_price, news_impact):
    """
    Decide buy/sell/hold based on prediction and news.
    :param predicted_price: LSTM predicted price.
    :param current_price: Latest price.
    :param news_impact: 'positive', 'negative', or 'neutral'.
    :return: 'buy', 'sell', or 'hold'.
    """
    if predicted_price > current_price * 1.02 and news_impact == "positive":
        return "buy"
    elif predicted_price < current_price * 0.98 and news_impact == "negative":
        return "sell"
    else:
        return "hold"