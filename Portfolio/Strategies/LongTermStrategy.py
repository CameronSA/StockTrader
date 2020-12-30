from Portfolio.TickerStatisticalAnalysis import TickerStatisticalAnalysis
from Simulation.LongTermIncreasingSimulation import LongTermIncreasingSimulation
from API.YahooFinance import StockTimeSeries
import numpy as np

class LongTermStrategy:
    def __init__(self, percentage_cash_out_limit, stock_exchange, time_period, interval):
        self.__percentage_cash_out_limit = percentage_cash_out_limit
        self.__stock_exchange = stock_exchange
        self.__time_period = time_period
        self.__interval = interval

    @property
    def percentage_cash_out_limit(self):
        return self.__percentage_cash_out_limit

    def analyse_security(self):
        # If stock price has increased, hold.
        # If stock price has decreased and reached cash out limit, sell.
        # Return action (hold/sell)
        pass

    def analyse_stock_exchange(self, ma_period, n_trials, shortlist_size, period, interval):
        ranked_stocks = self.__rank_stocks_by_gradient(ma_period, n_trials)
        if shortlist_size > len(ranked_stocks):
            shortlist_size = len(ranked_stocks)
        shortlisted_stocks = self.__shortlist_ranked_stocks(ranked_stocks[:shortlist_size], period, interval)
        return shortlisted_stocks

    def __rank_stocks_by_gradient(self, ma_period, n_trials):
        tckr = TickerStatisticalAnalysis(self.__time_period, self.__interval, self.__stock_exchange)
        trends_dict = tckr.trend_analysis(ma_period)
        ranked_tickers = tckr.rank_by_long_term_increasing(trends_dict, n_trials)
        return ranked_tickers

    def __shortlist_ranked_stocks(self, top_ranked_stocks, period, interval):
        percentage_returns = []
        shortlisted_stocks = []
        for ticker in top_ranked_stocks:
            long_term_increasing_sim = LongTermIncreasingSimulation(ticker, self.percentage_cash_out_limit)
            ohlc_data = StockTimeSeries().historical_data(ticker, period, interval)
            percentage_return = long_term_increasing_sim.run_long_term_increasing_strategy_sim(ohlc_data)
            percentage_returns.append((ticker, percentage_return))

        print('\nAll Returns:')
        return_values = []
        for percentage_return in percentage_returns:
            print(percentage_return)
            return_values.append(percentage_return[1])

        average_return = np.mean(return_values)
        stddev_return = np.std(return_values)
        print(f'\nAverage return = {average_return} +/- {stddev_return}')

        threshold_return = average_return
        if threshold_return <= 110:
            threshold_return = 110

        print(f'Threshold return = {threshold_return}')

        print(f'\nShortlist: ')
        for percentage_return in percentage_returns:
            if percentage_return[1] >= threshold_return:
                shortlisted_stocks.append(percentage_return[0])
                print(percentage_return)

        return shortlisted_stocks

