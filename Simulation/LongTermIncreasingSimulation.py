from datetime import datetime, timedelta
from API.YahooFinance import StockTimeSeries
from Finance.Bank import Bank
import numpy as np


class LongTermIncreasingSimulation:
    def __init__(self, ticker, sell_stop_percentage, term_period_days, start_date, end_date):
        self.__ticker = ticker
        self.__sell_stop_percentage = sell_stop_percentage
        self.__term_period_days = term_period_days
        self.__start_date = start_date
        self.__end_date = end_date

    @property
    def ticker(self):
        return self.__ticker

    @property
    def sell_stop_percentage(self):
        return self.__sell_stop_percentage

    @property
    def term_period_days(self):
        return self.__term_period_days

    @property
    def start_date(self):
        return self.__start_date

    @property
    def end_date(self):
        return self.__end_date

    def calculate_average_returns(self):
        # calculate average returns and error on returns over a time span

        # Find chunks of time with a given length over a given date range
        date_ranges = []
        returns = []
        date = self.start_date
        while date <= self.__end_date:
            start_date = date
            date = date + timedelta(days=self.term_period_days)
            date_ranges.append((start_date, date))

        for date_range in date_ranges:
            api = StockTimeSeries()
            ohlc_data = api.historical_data_timespan(self.ticker, date_range[0], date_range[1], '1d')
            bank_sim = Bank(10000)
            broker_fees = 0.01  # 1%
            count = 0
            print('New Trial')
            for index, row in ohlc_data.iterrows():
                sell = False
                open_price = row['Open']
                close_price = row['Close']
                cut_off_threshold = close_price - (close_price * self.sell_stop_percentage)
                # cut off can currently move in both directions. need to change so it can only go up

                if sell:
                    sell_fee = open_price*broker_fees
                    sell_price = open_price - sell_fee
                    bank_sim.sell_transaction(1, sell_price, f'"SELL {self.ticker}"')
                    break

                if count == 0:
                    buy_fee = open_price*broker_fees
                    buy_price = open_price + buy_fee
                    if buy_price <= bank_sim.current_balance:
                        bank_sim.buy_transaction(1, buy_price, f'"BUY {self.ticker}"')
                    else:
                        print('Stock too expensive')
                        break
                elif close_price < cut_off_threshold:
                    print("cut-off reached")
                    sell = True

                if count == len(ohlc_data) - 1:
                    sell_fee = open_price * broker_fees
                    sell_price = open_price - sell_fee
                    bank_sim.sell_transaction(1, sell_price, f'"SELL {self.ticker}"')
                    break

                count += 1

            percentage_return = 100*(bank_sim.current_balance/bank_sim.starting_balance)
            returns.append(percentage_return)

        average_return = np.mean(returns)
        stddev_return = np.std(returns)
        print(f'\nAVERAGE RETURN: {average_return} +/- {stddev_return}')