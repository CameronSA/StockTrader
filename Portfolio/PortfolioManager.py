from Portfolio.TickerAnalysis import TickerAnalysis
from AppSettings import *
import pandas as pd
from Objects.Security import Security
from Objects.Strategy import Strategy
from Portfolio.Strategies.LongTermStrategy import LongTermStrategy

class PortfolioManager:
    def __init__(self, stock_exchange):
        self.__stock_exchange = stock_exchange
        self.__stock_listings = TickerAnalysis('', '', stock_exchange).stock_listings
        if stock_exchange == 'snp500':
            self.__tracked_securities_path = SNP500_TRACKED_SECURITIES_PATH

        try:
            tracked_securities_df = pd.read_csv(self.tracked_securities_path)
            self.__tracked_securities = self.__df_to_securities(tracked_securities_df)
        except Exception as e:
            print(e)
            self.__tracked_securities = []


    @property
    def stock_exchange(self):
        return self.__stock_exchange

    @property
    def stock_listings(self):
        return self.__stock_listings

    @property
    def tracked_securities_path(self):
        return self.__tracked_securities_path

    @property
    def tracked_securities(self):
        return self.__tracked_securities

    @staticmethod
    def __df_to_securities(tracked_securities_df):
        securities = []
        for index, row in tracked_securities_df.iterrows():
            security = Security(row['stock_exchange'], row['ticker'], row['buy_price'], row['strategy'])
            securities.append(security)
        return securities

    def process_tracked_securities(self):
        for security in self.tracked_securities:
            if security.strategy == Strategy.long_term:
                pass



