from Portfolio.PortfolioManager import PortfolioManager
from Portfolio.Strategies.LongTermStrategy import LongTermStrategy
from Objects.StockExchanges import StockExchanges
from Finance.Bank import Bank


def main():
    bank = Bank(1000)
    percentage_cash_out_limit = 1
    portfolio = PortfolioManager(StockExchanges.SNP_500, percentage_cash_out_limit, bank)
    portfolio.process_tracked_securities()
    get_new_securities(portfolio, percentage_cash_out_limit)


def get_new_securities(portfolio, percentage_cash_out_limit):
    long_term_strategy = LongTermStrategy(percentage_cash_out_limit, StockExchanges.SNP_500)
    tickers_to_buy = long_term_strategy.analyse_stock_exchange()

    for ticker in tickers_to_buy:
        portfolio.buy_security(ticker)


if __name__ == '__main__':
    main()
