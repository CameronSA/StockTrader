import yfinance as yf


class StockTimeSeries:
    @staticmethod
    def historical_data(ticker, period, interval):
        tckr = yf.Ticker(ticker)
        return tckr.history(period=period, interval=interval)