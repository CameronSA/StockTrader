#import API.AlphaVantageConnection as avc
import API.YahooFinance as yahoo
import Indicators.Volatility as volatility

import Visualisation.Plotting as plotting

def main():
    ticker = 'IBM'
    ohlc_data = yahoo.StockTimeSeries.historical_data(ticker, '2y', '1d')
    volatility.BollingerBands.calculate(ohlc_data, 2, 20)
    bollinger_plot = plotting.BollingerPlot(ohlc_data, 'Close', 'bb_mavg', 'bb_upper', 'bb_lower',
                                            'bb_upper_ind', 'bb_lower_ind', 'bb_width',
                                            f'{ticker} Bollinger Bands')


if __name__ == '__main__':
    main()
