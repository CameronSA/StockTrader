from Portfolio.TickerAnalysis import TickerAnalysis
from AppSettings import *
import pandas as pd
from Objects.Security import Security
from Objects.Strategy import Strategy
from Objects.StockExchanges import StockExchanges
from Finance.FinancialActions import FinancialActions
from Portfolio.Strategies.LongTermStrategy import LongTermStrategy
from Objects.Actions import Actions


class PortfolioManager:
    def __init__(self, stock_exchange, long_term_percentage_cash_out_limit, bank):
        self.__stock_exchange = stock_exchange
        self.__stock_listings = TickerAnalysis('', '', stock_exchange).stock_listings
        self.__long_term_percentage_cash_out_limit = long_term_percentage_cash_out_limit
        self.__bank = bank
        if stock_exchange == StockExchanges.SNP_500:
            self.__tracked_securities_path = SNP500_TRACKED_SECURITIES_PATH

        try:
            tracked_securities_df = pd.read_csv(self.tracked_securities_path)
            self.__tracked_securities = self.__df_to_securities(tracked_securities_df)
        except Exception as e:
            print(e)
            self.__tracked_securities = []
        self.__updated_securities = []

    @property
    def bank(self):
        return self.__bank

    @property
    def updated_securities(self):
        return self.__updated_securities

    @property
    def long_term_percentage_cash_out_limit(self):
        return self.__long_term_percentage_cash_out_limit

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
            security = Security(row['stock_exchange'], row['ticker'], row['number_bought'],
                                row['buy_price'], row['strategy'])
            securities.append(security)
        return securities

    def process_tracked_securities(self):
        for security in self.tracked_securities:
            if security.strategy == Strategy.long_term:
                long_term_strategy = LongTermStrategy(self.long_term_percentage_cash_out_limit, self.stock_exchange)
                action = long_term_strategy.analyse_security()
                if action == Actions.hold:
                    self.__updated_securities.append(security)
                elif action == Actions.sell:
                    self.sell_security(security)
                else:
                    raise Exception("Invalid action received from security analysis")
            else:
                self.__updated_securities.append(security)

    def buy_security(self, ticker, number, strategy):
        buy_price = FinancialActions.buy(ticker, number)
        security = Security(self.stock_exchange, ticker, number, buy_price, strategy)
        self.__bank.buy_transaction(number, security.buy_price, f"BUY: {ticker}")
        self.__updated_securities.append(security)

    def sell_security(self, security):
        sell_price = FinancialActions.sell(security.ticker, security.number_bought)
        self.__bank.sell_transaction(security.number_bought, sell_price, f"SELL: {security.ticker}")

    def save_securities(self):
        with open(self.tracked_securities_path, 'w') as output_file:
            output_file.write('stock_exchange,ticker,number_bought,buy_price,strategy\n')
            for security in self.updated_securities:
                line_to_write = f'{security.stock_exchange}, {security.ticker}, {security.number_bought}, ' \
                                f'{security.buy_price}, {security.strategy}'
                output_file.write(line_to_write)
