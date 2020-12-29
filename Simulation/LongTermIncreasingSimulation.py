from datetime import datetime, timedelta
from API.YahooFinance import StockTimeSeries
from Finance.Bank import Bank


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
        date = self.start_date
        while date <= self.__end_date:
            start_date = date
            date = date + timedelta(days=self.term_period_days)
            date_ranges.append((start_date, date))

        for date_range in date_ranges:
            api = StockTimeSeries()
            ohlc_data = api.historical_data_timespan(self.ticker, date_range[0], date_range[1], '1d')
            bank_sim = Bank(100)
            broker_fees = 0.01  # 1%
            count = 0
            for index, row in ohlc_data.iterrows():
                open_price = row['Open']
                close_price = row['Close']
                cut_off_threshold = close_price - (close_price*self.sell_stop_percentage)
                if count == 0:
                    # need to delay this by 1 day
                    buy_fee = open_price*broker_fees
                    buy_price = open_price + buy_fee
                    bank_sim.buy_transaction(1, buy_fee, f'BUY {self.ticker}')
                elif close_price < cut_off_threshold:
                    pass
                else:
                    pass

                # sell at end if not already

                count += 1
