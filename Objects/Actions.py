class Actions:
    def __init__(self):
        self.__buy = 'buy'
        self.__sell = 'sell'
        self.__hold = 'hold'

    @property
    def buy(self):
        return self.__buy

    @property
    def sell(self):
        return self.__sell

    @property
    def hold(self):
        return self.__hold
