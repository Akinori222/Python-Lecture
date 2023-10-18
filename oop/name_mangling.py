class Account:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        self.show_balance()

    def withdraw(self, amount):
        if self.__balance < amount:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            self.show_balance()

    def show_balance(self):
        print(f"Your balance is ${self.__balance}.")


aki = Account(1000)
print(dir(aki))
aki.deposit(500)
aki.withdraw(2000)
# print(aki.__balance)  _Account__balance
aki.__balance = 2000  #
print(aki.__balance)
print(dir(aki))