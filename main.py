import API.AlphaVantageConnection as avc
import Visualisation.Plotting as plotting


def main():
    symbol = 'IBM'
    time_series = avc.StockTimeSeries(symbol=symbol)
    data = time_series.time_series_monthly()
    # ts_plot = plotting.TimeSeriesPlot()
    # ts_plot.add_series(data, 'timestamp', '1. open', 'open', 'blue', 'scatter')
    # ts_plot.add_series(data, 'timestamp', '2. high', 'high', 'green', 'scatter')
    # ts_plot.add_series(data, 'timestamp', '3. low', 'low', 'orange', 'scatter')
    # ts_plot.add_series(data, 'timestamp', '4. close', 'close', 'red', 'scatter')
    # ts_plot.draw('Price ($)', symbol)
    plotting.CandleStick().draw(data, '1. open', '2. high', '3. low', '4. close', '5. volume', 'timestamp')


if __name__ == '__main__':
    main()
