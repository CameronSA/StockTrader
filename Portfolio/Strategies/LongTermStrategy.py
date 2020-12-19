class LongTermStrategy:
    def analyse_security(self, percentage_cash_out_limit):
        # If stock price has increased, hold.
        # If stock price has decreased and reached cash out limit, sell.
        # Return action (hold/sell)
        pass

    def analyse_stock_exchange(self, stock_exchange):
        # Rank all tickers for stock exchange.
        # Buy any stock in top x that has not already been bought.
        # Return stocks to buy
        pass