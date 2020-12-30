import API.YahooFinance as yahoo
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
from tqdm import tqdm
from datetime import datetime
import time
from AppSettings import *
from Objects.StockExchanges import StockExchanges


class TickerStatisticalAnalysis:
    def __init__(self, time_period, interval, stock_exchange):
        self.__interval = interval
        self.__time_period = time_period
        self.__stock_exchange = stock_exchange
        self.__stock_listings = pd.read_csv(SNP500_STOCK_LISTINGS_PATH)

    @property
    def stock_exchange(self):
        return self.__stock_exchange

    @property
    def stock_listings(self):
        return self.__stock_listings

    def trend_analysis(self, ma_period):
        print(f'Performing trend analysis for {self.stock_exchange}. . .')
        time.sleep(0.05)
        trend_gradient_analysis_dict = {}
        # count = 0
        for ticker in tqdm(self.stock_listings['Symbol']):
            # if count >= 20:
            #     break
            self.__trend_gradient_analysis(trend_gradient_analysis_dict, ticker, ma_period)
            # count += 1
        return trend_gradient_analysis_dict

    def rank_by_long_term_increasing(self, trend_gradient_analysis_dict, n_trials):
        tickers = []
        trend_gradients = []
        trend_gradient_errors = []
        for ticker in list(trend_gradient_analysis_dict.keys()):
            gradient_analysis = trend_gradient_analysis_dict[ticker]
            popt = gradient_analysis[0]
            pcov = gradient_analysis[1]
            popt_error = np.sqrt(np.diag(pcov))

            trend_gradient = popt[0]
            trend_gradient_error = popt_error[0]
            tickers.append(ticker)
            trend_gradients.append(trend_gradient)
            trend_gradient_errors.append(trend_gradient_error)

        ticker_trends_df = pd.DataFrame({'Key': tickers,
                                      'Trend Gradient': trend_gradients,
                                      'Trend Gradient Error': trend_gradient_errors})

        # To take account of errors: rank tickers by gradient where each gradient is taken from a normal distribution
        # where the mean is the gradient and the standard deviation is the error on the gradient. Repeat this N times.
        # For each trial, note the position of each ticker.
        # The ticker's final ranking is the average of all of it's positions rounded to the nearest int. Duplicate
        # rankings are put in a random order
        ticker_average_rankings_dict = self.__perform_monte_carlo_ranking(ticker_trends_df, n_trials)
        ranked_ticker_tuples = sorted(ticker_average_rankings_dict.items(), key=lambda x: x[1], reverse=False)
        ranked_tickers = []
        for tpl in ranked_ticker_tuples:
            ranked_tickers.append(tpl[0])
        return ranked_tickers

    def __perform_monte_carlo_ranking(self, ticker_trends_df, n_trials):
        def __perform_unit_simulation(ticker_trends_df):
            simulated_df = ticker_trends_df
            simulated_fit_values = []
            for index, row in simulated_df.iterrows():
                simulated_fit_values.append(np.random.normal(row['Trend Gradient'], row['Trend Gradient Error']))

            simulated_df['Simulated Gradient'] = simulated_fit_values
            simulated_df.sort_values('Simulated Gradient', ascending=False, inplace=True)
            simulated_df.reset_index(drop=True, inplace=True)
            simulated_df['Ranking'] = simulated_df.index
            simulated_dict = {}
            for index, row in simulated_df.iterrows():
                simulated_dict[row['Key']] = row['Ranking']
            return simulated_dict

        rankings_list_dict = {}
        print('Performing Monte Carlo Ranking Simulation. . .')
        time.sleep(0.05)
        for i in tqdm(range(0, n_trials)):
            ticker_rankings_dict = __perform_unit_simulation(ticker_trends_df)
            for ticker, ranking in ticker_rankings_dict.items():
                if ticker in rankings_list_dict:
                    rankings_list_dict[ticker].append(ranking)
                else:
                    rankings_list_dict[ticker] = [ranking]

        average_rankings_dict = {}
        for ticker, rankings_list in rankings_list_dict.items():
            average_ranking = float(np.mean(rankings_list))
            average_rankings_dict[ticker] = int(round(average_ranking))

        return average_rankings_dict

    def __straight_line(self, x, m, c):
        return m*x + c

    def __trend_gradient_analysis(self, trend_analysis_dict, ticker, ma_period):
        ohlc_data = pd.DataFrame()
        try:
            ohlc_data = yahoo.StockTimeSeries.historical_data(ticker, self.__time_period, self.__interval)
        except Exception as e:
            print(f'- Error encountered for ticker: {ticker}: ', e)
        if not ohlc_data.empty:
            analysed_data = pd.DataFrame()
            analysed_data['MA'] = ohlc_data['Close'].rolling(window=ma_period).mean().dropna()
            analysed_data['UTC'] = analysed_data.index

            def utc_time_difference(time):
                start = datetime(1970, 1, 1, 12, 0, 0, 0)
                elapsed_time = time-start
                return elapsed_time.total_seconds()

            analysed_data['UTC'] = analysed_data['UTC'].apply(lambda x: utc_time_difference(x))
            try:
                popt, pcov = curve_fit(self.__straight_line, analysed_data.UTC, analysed_data.MA)
                results = (popt, pcov)
                if ticker not in trend_analysis_dict.keys():
                    trend_analysis_dict[ticker] = results
                else:
                    print(f'WARNING: Duplicate tickers found: {ticker}')
            except Exception as e:
                print(f'- Error encountered for ticker {ticker}', e)
