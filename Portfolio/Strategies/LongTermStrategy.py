from Portfolio.TickerStatisticalAnalysis import TickerAnalysis
from Simulation.LongTermIncreasingSimulation import LongTermIncreasingSimulation


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

    def analyse_stock_exchange(self, ma_period, n_trials, shortlist_size, term_period,
                               start_date, end_date):
        ranked_stocks = self.__rank_stocks_by_gradient(ma_period, n_trials)
        if shortlist_size < len(ranked_stocks):
            shortlist_size = ranked_stocks
        shortlisted_stocks = self.__shortlist_ranked_stocks(ranked_stocks[:shortlist_size],
                                                            term_period, start_date, end_date)

    def __rank_stocks_by_gradient(self, ma_period, n_trials):
        tckr = TickerAnalysis(self.__time_period, self.__interval, self.__stock_exchange)
        trends_dict = tckr.trend_analysis(ma_period)
        ranked_tickers = tckr.rank_by_long_term_increasing(trends_dict, n_trials)
        return ranked_tickers

    def __shortlist_ranked_stocks(self, top_ranked_stocks, term_period, start_date, end_date):
        shortlisted_stocks = []
        for ticker in top_ranked_stocks:
            long_term_increasing_sim = LongTermIncreasingSimulation(ticker, self.percentage_cash_out_limit,
                                                                    term_period, start_date, end_date)
            returns, stddev = long_term_increasing_sim.calculate_average_returns()
            if returns - (2*stddev) > 0:
                shortlisted_stocks.append(ticker)

        return shortlisted_stocks

