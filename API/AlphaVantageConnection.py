import pandas as pd
import requests


class Credentials:
    def __init__(self):
        self.api_key = 'ZNQ9U6GP44W5YTBK'
        self.base_url = 'https://www.alphavantage.co/'


class StockTimeSeries(Credentials):
    def __init__(self, symbol):
        Credentials.__init__(self)
        self.__symbol = symbol

    @staticmethod
    def __read_results(url, time_series_key):
        __response = requests.get(url)
        __dict = __response.json()[time_series_key]
        __df = pd.DataFrame.from_dict(__dict).transpose()
        __df['timestamp'] = pd.to_datetime(__df.index, format='%Y-%m-%d %H:%M:%S')
        __df = __df.sort_values('timestamp')
        return __df

    def time_series_intraday(self, interval_min):
        __url = f'{self.base_url}query?function=TIME_SERIES_INTRADAY&symbol={self.__symbol}&interval={interval_min}min&apikey={self.api_key}'
        return self.__read_results(__url, f'Time Series ({interval_min}min)')

    def time_series_intraday_extended(self, interval_min, year_slice, ):
        raise Exception('Function unavailable')

    def time_series_daily(self):
        __url = f'{self.base_url}query?function=TIME_SERIES_DAILY&symbol={self.__symbol}&apikey={self.api_key}'
        return self.__read_results(__url, f'Time Series (Daily)')

    def time_series_daily_adjusted(self):
        __url = f'{self.base_url}query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={self.__symbol}&apikey={self.api_key}'
        return self.__read_results(__url, f'Time Series (Daily)')

    def time_series_weekly(self):
        __url = f'{self.base_url}query?function=TIME_SERIES_WEEKLY&symbol={self.__symbol}&apikey={self.api_key}'
        return self.__read_results(__url, f'Weekly Time Series')

    def time_series_weekly_adjusted(self):
        __url = f'{self.base_url}query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={self.__symbol}&apikey={self.api_key}'
        return self.__read_results(__url, f'Weekly Adjusted Time Series')

    def time_series_monthly(self):
        __url = f'{self.base_url}query?function=TIME_SERIES_MONTHLY&symbol={self.__symbol}&apikey={self.api_key}'
        return self.__read_results(__url, f'Monthly Time Series')

    def time_series_monthly_adjusted(self):
        __url = f'{self.base_url}query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={self.__symbol}&apikey={self.api_key}'
        return self.__read_results(__url, f'Monthly Adjusted Time Series')


class Endpoint(Credentials):

    def quote_endpoint(self, __symbol):
        __url = f'{self.base_url}query?function=GLOBAL_QUOTE&symbol={__symbol}&apikey={self.api_key}'
        return pd.read_json(__url).transpose()

    def search_endpoint(self, keyword):
        __url = f'{self.base_url}query?function=SYMBOL_SEARCH&keywords={keyword}&apikey={self.api_key}'
        __response = requests.get(__url)
        __dict = __response.json()['bestMatches']
        return pd.DataFrame.from_dict(__dict)