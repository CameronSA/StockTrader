class Bank:
    def __init__(self, starting_balance):
        self.__starting_balance = starting_balance
        self.__current_balance = starting_balance

    @property
    def starting_balance(self):
        return self.__starting_balance

    @property
    def current_balance(self):
        return self.__current_balance

    def buy_transaction(self, number, price, action):
        self.__current_balance -= price
        print("Action", "Number", "Amount", "Resulting Balance")
        print(action, number, f'-{price}', self.current_balance)

    def sell_transaction(self, number, price, action):
        self.__current_balance += price
        print("Action", "Number", "Amount", "Resulting Balance")
        print(action, number, price, self.current_balance)
