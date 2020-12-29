import yfinance as yf


class StockTimeSeries:
    @staticmethod
    def historical_data(ticker, period, interval):
        tckr = yf.Ticker(ticker)
        return tckr.history(period=period, interval=interval)

    @staticmethod
    def historical_data_timespan(ticker, start_time, end_time, interval):
        tckr = yf.Ticker(ticker)
        return tckr.history(start=start_time, end=end_time, interval=interval)

