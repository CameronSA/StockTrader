class LongTermStrategy:
    def __init__(self, percentage_cash_out_limit, stock_exchange):
        self.__percentage_cash_out_limit = percentage_cash_out_limit
        self.__stock_exchange = stock_exchange

    def analyse_security(self):
        # If stock price has increased, hold.
        # If stock price has decreased and reached cash out limit, sell.
        # Return action (hold/sell)
        pass

    def analyse_stock_exchange(self):
        # Rank all tickers for stock exchange.
        # Buy any stock in top x that has not already been bought.
        # Return stocks to buy
        pass
