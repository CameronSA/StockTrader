import API.YahooFinance as yahoo
import pandas as pd
import numpy as np
from scipy.stats import skew, skewtest
import pandas as pd
from numpy import diff
from tqdm import tqdm


class TickerAnalysis:
    def __init__(self, time_period, interval):
        self.__interval = interval
        self.__time_period = time_period

    def __set_stock_exchange(self, stock_exchange):
        if stock_exchange == 'snp500':
            self.__stock_listings = pd.read_csv('StockListings/SNP500_Listings_2020-11-22.csv')

    def calculate_returns(self, ticker):
        ohlc_data = yahoo.StockTimeSeries.historical_data(ticker, self.__time_period, self.__interval)
        returns_data = ohlc_data['Close'].pct_change().dropna()
        returns = {
            'returns_data': returns_data,
            'returns_mean': np.mean(returns_data),
            'returns_stddev': np.std(returns_data),
            'returns_median': np.quantile(returns_data, 0.5),
            'returns_skewness': skew(returns_data),
            'returns_skewtest': skewtest(returns_data)}

        return returns

    def trend_analysis(self, stock_exchange, ma_period):
        print('Performing trend analysis for SNP500. . .')
        self.__set_stock_exchange(stock_exchange)
        trend_analysis_dict = {}
        for ticker in tqdm(self.__stock_listings['Symbol']):
            ohlc_data = pd.DataFrame()
            analysed_data = pd.DataFrame()
            try:
                ohlc_data = yahoo.StockTimeSeries.historical_data(ticker, self.__time_period, self.__interval)
            except Exception as e:
                print(f'Error encountered for ticker: {ticker}: ', e)
            if not ohlc_data.empty:
                analysed_data = pd.DataFrame()
                analysed_data['MA'] = ohlc_data['Close'].rolling(window=ma_period).mean()
                derivative = list(diff(analysed_data['MA'])/diff(ohlc_data.index.astype(int)*(10**-9)))
                derivative.insert(0, np.nan)
                analysed_data['dMA'] = derivative
                analysed_data['dMA_MA'] = analysed_data['dMA'].rolling(window=ma_period).mean()
                if ticker not in trend_analysis_dict.keys():
                    trend_analysis_dict[ticker] = analysed_data
                else:
                    print(f'WARNING: Duplicate tickers found: {ticker}')
            break
        return trend_analysis_dict

    @staticmethod
    def select_from_trend_analysis(trend_analysis_dict):
        for key, value in trend_analysis_dict.items():
            break
