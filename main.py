from Portfolio.PortfolioManager import PortfolioManager
from Portfolio.Strategies.LongTermStrategy import LongTermStrategy
from Objects.StockExchanges import StockExchanges
from Finance.Bank import Bank
import tests


def main():
    #manage_portfolio()

    #tests.test_indicators()
    #tests.test_optimise_long_term_increasing_cut_off()
    #tests.test_long_term_increasing_sim('MSFT', 10)
    tests.test_long_term_increasing_ranking()

def manage_portfolio():
    shortlist_size = 10
    number_stocks_to_buy = 1
    data_time_period = '5y'
    data_interval = '1d'

    ma_period_for_initial_ranking = 100
    n_trials_for_initial_ranking = 100

    long_term_increasing_sell_stop_percentage = 1
    bank = Bank(1000)

    portfolio = PortfolioManager(StockExchanges().SNP_500, bank)
    portfolio.process_tracked_securities(data_interval, data_time_period)
    long_term_strategy = LongTermStrategy(long_term_increasing_sell_stop_percentage, StockExchanges().SNP_500,
                                          data_time_period, data_interval)
    tickers_to_buy = long_term_strategy.analyse_stock_exchange(ma_period_for_initial_ranking,
                                                               n_trials_for_initial_ranking, shortlist_size,
                                                               data_time_period, data_interval)

    for ticker in tickers_to_buy:
        portfolio.buy_security(ticker, number_stocks_to_buy)
    portfolio.save_securities()


if __name__ == '__main__':
    main()
