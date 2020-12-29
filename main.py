from Portfolio.PortfolioManager import PortfolioManager
from Portfolio.Strategies.LongTermStrategy import LongTermStrategy
from Objects.StockExchanges import StockExchanges
from Finance.Bank import Bank
from API.YahooFinance import StockTimeSeries
from datetime import datetime


def main():
    #manage_portfolio()
    #test_indicators()
    test_long_term_increasing_sim()

def test_long_term_increasing_sim():
    from Simulation.LongTermIncreasingSimulation import LongTermIncreasingSimulation
    sim = LongTermIncreasingSimulation('AMZN', 1, 365, datetime(2000, 1, 1), datetime(2019, 12, 31))
    sim.calculate_average_returns()


def test_indicators():
    from Indicators import Momentum
    from Indicators import Trend
    from Indicators import Volatility
    from Visualisation import Plotting

    ticker = 'IBM'
    series = StockTimeSeries()
    data = series.historical_data(ticker, '1y', '1d')
    Momentum.RelativeStrengthIndex.calculate(data)
    Trend.MACD.calculate(data)
    Volatility.BollingerBands.calculate(data, 2, 20)

    rsi_plot = Plotting.RSIPlot(data, 'Close', 'rsi', 'rsi_signal', 'strong_rsi_signal', f'{ticker} RSI')
    bollinger_plot = Plotting.BollingerPlot(data, 'Close', 'bb_mavg', 'bb_upper', 'bb_lower',
                                            'bb_signal', 'bb_width', f'{ticker} Bollinger Bands')
    macd_plot = Plotting.MACDPlot(data, 'Close', 'macd', 'macd_ema', 'macd_diff', 'macd_signal',
                                  'ema_short', 'ema_long', 'ema_signal', f'{ticker} EMA and MACD')


def manage_portfolio():
    shortlist_size = 10
    number_stocks_to_buy = 1
    data_time_period = '5y'
    data_interval = '1d'

    ma_period_for_initial_ranking = 100
    n_trials_for_initial_ranking = 100

    long_term_increasing_sell_stop_percentage = 1
    sim_period_days = 365
    sim_start_date = datetime(2000, 1, 1)
    sim_end_date = datetime(2019, 12, 31)

    bank = Bank(1000)

    portfolio = PortfolioManager(StockExchanges.SNP_500, bank)
    portfolio.process_tracked_securities(data_interval, data_time_period)
    long_term_strategy = LongTermStrategy(long_term_increasing_sell_stop_percentage, StockExchanges.SNP_500,
                                          data_time_period, data_interval)
    tickers_to_buy = long_term_strategy.analyse_stock_exchange(ma_period_for_initial_ranking,
                                                               n_trials_for_initial_ranking, shortlist_size,
                                                               sim_period_days, sim_start_date, sim_end_date)

    for ticker in tickers_to_buy:
        portfolio.buy_security(ticker, number_stocks_to_buy)
    portfolio.save_securities()


if __name__ == '__main__':
    main()
    #data = StockTimeSeries().historical_data('MSFT', '1d', '1d')
    #print(float(data.Open[0]))
