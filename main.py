#import API.AlphaVantageConnection as avc
import API.YahooFinance as yahoo
import Indicators.Volatility as volatility
import Indicators.Momentum as momentum
import Indicators.Trend as trend

import Visualisation.Plotting as plotting

def main():
    ticker = 'MSFT'
    ohlc_data = yahoo.StockTimeSeries.historical_data(ticker, '2y', '1d')
    momentum.RelativeStrengthIndex.calculate(ohlc_data)
    volatility.BollingerBands.calculate(ohlc_data, 2, 20)
    trend.MACD.calculate(ohlc_data)
    rsi_plot = plotting.RSIPlot(ohlc_data, 'Close', 'rsi', f'{ticker} RSI')
    bollinger_plot = plotting.BollingerPlot(ohlc_data, 'Close', 'bb_mavg', 'bb_upper', 'bb_lower',
                                            'bb_upper_ind', 'bb_lower_ind', 'bb_width',
                                            f'{ticker} Bollinger Bands', True)
    macd_plot = plotting.MACDPlot(ohlc_data, 'Close', 'macd', 'macd_sig', 'macd_diff', 'ema_short', 'ema_long',f'{ticker} MACD')


if __name__ == '__main__':
    main()
