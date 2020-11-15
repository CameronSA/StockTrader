#import API.AlphaVantageConnection as avc
import API.YahooFinance as yahoo
import Indicators.Volatility as volatility
import Indicators.Momentum as momentum
import Indicators.Trend as trend
import Indicators.ApplyIndicators as apply
from Portfolio.TickerAnalysis import TickerAnalysis

import Visualisation.Plotting as plotting

def main():
    ticker = 'AMZN'
    ohlc_data = yahoo.StockTimeSeries.historical_data(ticker, '10y', '1d')
    apply.apply_indicators(ohlc_data)
    close_data = ohlc_data.drop(columns=['Open', 'High', 'Low', 'Volume', 'Dividends', 'Stock Splits'])
    tckr = TickerAnalysis(ticker, '2y', '1d')
    returns_dict = tckr.calculate_returns()
    print(returns_dict)

    plotting.RSIPlot(close_data, 'Close', 'rsi', 'rsi_signal', 'strong_rsi_signal', f'{ticker} RSI')
    plotting.Histogram(returns_dict['returns_data'], f'{ticker} % returns')
    # plotting.BollingerPlot(close_data, 'Close', 'bb_mavg', 'bb_upper', 'bb_lower',
    #                        'bb_signal', 'bb_width', f'{ticker} Bollinger Bands')
    # plotting.MACDPlot(close_data, 'Close', 'macd', 'macd_ema', 'macd_diff', 'macd_signal',
    #                               'ema_short', 'ema_long', 'ema_signal', f'{ticker} EMA and MACD')


if __name__ == '__main__':
    main()
