import API.AlphaVantageConnection as avc
import Visualisation.Plotting as plotting
from LogicHelpers.CommonFunctions import to_ohlc
import Indicators.DojiScan as doji

def main():
    symbol = 'MSFT'
    time_series = avc.StockTimeSeries(symbol=symbol)
    data = time_series.time_series_daily()
    # ts_plot = plotting.TimeSeriesPlot()
    # ts_plot.add_series(data, 'timestamp', '1. open', 'open', 'blue', 'scatter')
    # ts_plot.add_series(data, 'timestamp', '2. high', 'high', 'green', 'scatter')
    # ts_plot.add_series(data, 'timestamp', '3. low', 'low', 'orange', 'scatter')
    # ts_plot.add_series(data, 'timestamp', '4. close', 'close', 'red', 'scatter')
    # ts_plot.draw('Price ($)', symbol)
    ohlc_data = to_ohlc(data, '1. open', '2. high', '3. low', '4. close', 'timestamp')
    doji_data = doji.DojiScan(ohlc_data)
    plotting.CandleStick().draw(ohlc_data)
    doji_plot = plotting.TimeSeriesPlot()
    doji_plot.add_series(doji_data, 'Date', 'Doji', 'Doji', 'blue', 'line')
    doji_plot.draw('Doji', symbol)
    input('Press [enter] to continue. . .')


if __name__ == '__main__':
    main()
