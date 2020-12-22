class Security:
    def __init__(self, stock_exchange, ticker, number_bought, buy_price, strategy):
        self.__stock_exchange = stock_exchange
        self.__ticker = ticker
        self.__number_bought = number_bought
        self.__buy_price = buy_price
        self.__strategy = strategy

    @property
    def stock_exchange(self):
        return self.__stock_exchange

    @property
    def ticker(self):
        return self.__ticker

    @property
    def number_bought(self):
        return self.__number_bought

    @property
    def buy_price(self):
        return self.__ticker

    @property
    def strategy(self):
        return self.__strategy
