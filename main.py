#import API.AlphaVantageConnection as avc
import API.YahooFinance as yahoo
import Indicators.Volatility as volatility
import Indicators.Momentum as momentum
import Indicators.Trend as trend
import Indicators.ApplyIndicators as apply
from Portfolio.TickerAnalysis import TickerAnalysis

import Visualisation.Plotting as plotting

def main():


    #ticker = 'MMM'
    #ohlc_data = yahoo.StockTimeSeries.historical_data(ticker, '2y', '1d')
    #apply.apply_indicators(ohlc_data)
    #close_data = ohlc_data.drop(columns=['Open', 'High', 'Low', 'Volume', 'Dividends', 'Stock Splits'])

    # tckr = TickerAnalysis('5y', '1d')
    # trend_gradient_analysis_dict = tckr.trend_analysis('snp500', ma_period=100)
    # ranked_tickers = tckr.rank_by_trend(trend_gradient_analysis_dict, 1000)

    # count = 0
    # for ticker in ranked_tickers:
    #     if count % 20 == 0:
    #         ohlc_data = yahoo.StockTimeSeries.historical_data(ticker, '5y', '1d')
    #         ts_plot = plotting.TimeSeriesPlot()
    #         ts_plot.add_series(ohlc_data, 'Close', 'Close Price', 'blue')
    #         ts_plot.draw('Price ($)', ticker)
    #     count += 1

    # returns = tckr.calculate_returns()
    # print(returns)
    # plotting.Histogram(returns['returns_data'], f'{ticker} % returns')

    # plotting.RSIPlot(close_data, 'Close', 'rsi', 'rsi_signal', 'strong_rsi_signal', f'{ticker} RSI')
    # plotting.BollingerPlot(close_data, 'Close', 'bb_mavg', 'bb_upper', 'bb_lower',
    #                        'bb_signal', 'bb_width', f'{ticker} Bollinger Bands')
    # plotting.MACDPlot(close_data, 'Close', 'macd', 'macd_ema', 'macd_diff', 'macd_signal',
    #                               'ema_short', 'ema_long', 'ema_signal', f'{ticker} EMA and MACD')

if __name__ == '__main__':
    main()
