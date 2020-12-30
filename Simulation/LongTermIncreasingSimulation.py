from datetime import datetime, timedelta
from API.YahooFinance import StockTimeSeries
from Finance.Bank import Bank
import numpy as np


class LongTermIncreasingSimulation:
    def __init__(self, ticker, sell_stop_percentage):
        self.__ticker = ticker
        self.__sell_stop_percentage = sell_stop_percentage

    @property
    def ticker(self):
        return self.__ticker

    @property
    def sell_stop_percentage(self):
        return self.__sell_stop_percentage

    def run_long_term_increasing_strategy_sim(self, ohlc_data):
        bank_sim = Bank(1000)
        broker_fees = 0.01  # 1%
        count = 0
        highest_cut_off_threshold = -1
        highest_cut_off_threshold_set = False
        sell = False
        for index, row in ohlc_data.iterrows():
            open_price = row['Open']
            close_price = row['Close']
            cut_off_threshold = close_price - (close_price * (self.sell_stop_percentage/100))
            if cut_off_threshold > highest_cut_off_threshold or not highest_cut_off_threshold_set:
                highest_cut_off_threshold = cut_off_threshold
                highest_cut_off_threshold_set = True

            if sell:
                sell_fee = open_price * broker_fees
                sell_price = open_price - sell_fee
                bank_sim.sell_transaction(1, sell_price, f'"SELL {self.ticker}"')
                break

            if count == 0:
                buy_fee = open_price * broker_fees
                buy_price = open_price + buy_fee
                bank_sim.buy_transaction(1, buy_price, f'"BUY {self.ticker}"')
            elif close_price < highest_cut_off_threshold:
                print("cut-off reached")
                # need to implement indicator strategy here
                sell = True

            if count == len(ohlc_data) - 1:
                sell_fee = open_price * broker_fees
                sell_price = open_price - sell_fee
                bank_sim.sell_transaction(1, sell_price, f'"SELL {self.ticker}"')
                break

            count += 1

        percentage_return = 100 * (bank_sim.current_balance / bank_sim.starting_balance)
        print(f'RETURN: {percentage_return}')
        return percentage_return
