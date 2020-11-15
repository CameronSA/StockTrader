import API.YahooFinance as yahoo
import pandas as pd
import numpy as np
from scipy.stats import skew, skewtest

class TickerAnalysis:
    def __init__(self, ticker, time_period, interval):
        self.__ticker = ticker
        self.__interval = interval
        self.__time_period = time_period

    def calculate_returns(self):
        ohlc_data = yahoo.StockTimeSeries.historical_data(self.__ticker, self.__time_period, self.__interval)
        returns_data = ohlc_data['Close'].pct_change().dropna()
        returns = {
            'returns_data': returns_data,
            'returns_mean': np.mean(returns_data),
            'returns_stddev': np.std(returns_data),
            'returns_median': np.quantile(returns_data, 0.5),
            'returns_skewness': skew(returns_data),
            'returns_skewtest': skewtest(returns_data)}

        return returns
