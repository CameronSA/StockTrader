class Security:
    def __init__(self, stock_exchange, ticker, buy_price, strategy):
        self.__stock_exchange = stock_exchange
        self.__ticker = ticker
        self.__buy_price = buy_price
        self.__strategy = strategy

    @property
    def stock_exchange(self):
        return self.__stock_exchange

    @property
    def ticker(self):
        return self.__ticker

    @property
    def buy_price(self):
        return self.__ticker

    @property
    def strategy(self):
        return self.__strategy
