from Portfolio.PortfolioManager import PortfolioManager
from Portfolio.Strategies.LongTermStrategy import LongTermStrategy
from Objects.StockExchanges import StockExchanges
from Finance.Bank import Bank
from API.YahooFinance import StockTimeSeries
from Indicators import Momentum
from Indicators import Trend
from Indicators import Volatility
from Visualisation import Plotting


def main():
    #manage_portfolio()
    test_indicators()


def test_indicators():
    ticker = 'MSFT'
    series = StockTimeSeries()
    data = series.historical_data(ticker, '5y', '1d')
    Momentum.RelativeStrengthIndex.calculate(data)
    Trend.MACD.calculate(data)
    Volatility.BollingerBands.calculate(data, 2, 20)

    rsi_plot = Plotting.RSIPlot(data, 'Close', 'rsi', 'rsi_signal', 'strong_rsi_signal', f'{ticker} RSI')
    bollinger_plot = Plotting.BollingerPlot(data, 'Close', 'bb_mavg', 'bb_upper', 'bb_lower',
                                            'bb_signal', 'bb_width', f'{ticker} Bollinger Bands')
    macd_plot = Plotting.MACDPlot(data, 'Close', 'macd', 'macd_ema', 'macd_diff', 'macd_signal',
                                  'ema_short', 'ema_long', 'ema_signal', f'{ticker} EMA and MACD')


def manage_portfolio():
    time_period = '5y'
    interval = '1d'
    ma_period = 100
    n_trials = 100
    bank = Bank(1000)
    percentage_cash_out_limit = 1
    portfolio = PortfolioManager(StockExchanges.SNP_500, percentage_cash_out_limit, bank)
    portfolio.process_tracked_securities()
    __get_new_securities(portfolio, percentage_cash_out_limit, time_period, interval, n_trials)
    portfolio.save_securities()


def __get_new_securities(portfolio, percentage_cash_out_limit, time_period, interval, ma_period, n_trials):
    long_term_strategy = LongTermStrategy(percentage_cash_out_limit, StockExchanges.SNP_500, time_period, interval)
    tickers_to_buy = long_term_strategy.analyse_stock_exchange(ma_period, n_trials)

    for ticker in tickers_to_buy:
        portfolio.buy_security(ticker)


if __name__ == '__main__':
    main()
    #data = StockTimeSeries().historical_data('MSFT', '1d', '1d')
    #print(float(data.Open[0]))
