class Bank:
    def __init__(self, starting_balance):
        self.__starting_balance = starting_balance
        self.__current_balance = starting_balance

    @property
    def starting_balance(self):
        return self.__starting_balance

    def current_balance(self):
        return self.__current_balance

    def buy_transaction(self, price, reference):
        self.__current_balance -= price
        print("Reference", "Amount", "Resulting Balance")
        print(reference, f'-{price}', self.current_balance())

    def sell_transaction(self, price, reference):
        self.__current_balance += price
        print("Reference", "Amount", "Resulting Balance")
        print(reference, price, self.current_balance())
