from Simulation.LongTermIncreasingSimulation import LongTermIncreasingSimulation
import matplotlib.pyplot as plt
from API.YahooFinance import StockTimeSeries
from Portfolio.Strategies.LongTermStrategy import LongTermStrategy
from Objects.StockExchanges import StockExchanges

def test_long_term_increasing_ranking():
    shortlist_size = 30
    data_time_period = '2y'
    data_interval = '1d'
    ma_period_for_initial_ranking = 100
    n_trials_for_initial_ranking = 100
    long_term_increasing_sell_stop_percentage = 10

    long_term_strategy = LongTermStrategy(long_term_increasing_sell_stop_percentage, StockExchanges().SNP_500,
                                          data_time_period, data_interval)
    tickers_to_buy = long_term_strategy.analyse_stock_exchange(ma_period_for_initial_ranking,
                                                               n_trials_for_initial_ranking, shortlist_size,
                                                               data_time_period, data_interval)

def test_optimise_long_term_increasing_cut_off():
    x_vals = []
    y_vals = []
    ticker = 'WLL'
    for i in range(1, 100):
        percentage_return = test_long_term_increasing_sim(ticker, i/2)
        x_vals.append(i/2)
        y_vals.append(percentage_return)

    plt.plot(x_vals, y_vals)
    plt.xlabel('cut-off (%)')
    plt.ylabel('return (%)')
    plt.show()


def test_long_term_increasing_sim(ticker, cut_off_percentage):
    sim = LongTermIncreasingSimulation(ticker, cut_off_percentage)
    ohlc_data = StockTimeSeries().historical_data(ticker, '2y', '1d')
    percentage_return = sim.run_long_term_increasing_strategy_sim(ohlc_data)
    # strategy is incomplete as no action is taken to recover from a stop loss (i.e. buy again when indicators say so).
    # This will need to be added in when the code is written.

    return percentage_return


def test_indicators():
    from Indicators import Momentum
    from Indicators import Trend
    from Indicators import Volatility
    from Visualisation import Plotting

    ticker = 'IBM'
    series = StockTimeSeries()
    data = series.historical_data(ticker, '2y', '1d')
    Momentum.RelativeStrengthIndex.calculate(data)
    Trend.MACD.calculate(data)
    Volatility.BollingerBands.calculate(data, 2, 20)

    rsi_plot = Plotting.RSIPlot(data, 'Close', 'rsi', 'rsi_signal', 'strong_rsi_signal', f'{ticker} RSI')
    bollinger_plot = Plotting.BollingerPlot(data, 'Close', 'bb_mavg', 'bb_upper', 'bb_lower',
                                            'bb_signal', 'bb_width', f'{ticker} Bollinger Bands')
    macd_plot = Plotting.MACDPlot(data, 'Close', 'macd', 'macd_ema', 'macd_diff', 'macd_signal',
                                  'ema_short', 'ema_long', 'ema_signal', f'{ticker} EMA and MACD')
