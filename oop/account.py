import time


class Account:

    count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.account_number = Account.count
        self.show_balance()
        self.transaction_history = []
        Account.count += 1

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance!!")
        else:
            self.balance -= amount
            print(f"Balance is {self.balance} yen.")
            self.show_balance()
            self._add_transaction(-amount)

    def deposit(self, amount):
        self.balance += amount
        self.show_balance()
        self._add_transaction(amount)

    def show_balance(self):
        print(f"{self.name}({self.account_number})'s balance is {self.balance} yen. ")

    def _add_transaction(self, amount):
        transaction = {
            "withdraw/deposit": amount,
            "new_balance": self.balance,
            "time": Account._get_time_str()
        }
        self.transaction_history.append(transaction)

    @staticmethod
    def _get_time_str():
        current_time = time.localtime()
        return "{0.tm_year}年{0.tm_mon}月{0.tm_mday}日{0.tm_hour}時{0.tm_min}分".format(current_time)

    def show_transaction_history(self):
        for transaction in self.transaction_history:
            transaction_str_list = []
            for k, v in transaction.items():
                transaction_str_list.append( f"{k}, {v}")
            print(", ".join(transaction_str_list))


akinori = Account("akinori", 1000)
kato = Account("Kato", 2000)

print(akinori.name)
print(akinori.balance)
akinori.withdraw(500)
akinori.deposit(200)
akinori.withdraw(2000)
print(kato.balance)
print(akinori.transaction_history)
print(Account._get_time_str())
akinori.show_transaction_history()