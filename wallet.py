# chunk 1: class creation and encapsulation
class Digital_Wallet:
    def __init__(self, wallet_id, owner_name, balance=0):
        self.wallet_id = wallet_id
        self.owner_name = owner_name
        if balance < 0:
            print("Balance cannot be negative. Setting balance to 0.")
            self.__balance = 0
        else:
            self.__balance = balance

        #no parameter bcoz there's no history when wallet is being created 
        self.__transaction_history = []
        self.__transaction_id = 1

    #chunk 2: wallet display
    def get_balance(self):
        copy_balance = self.__balance
        return copy_balance

    def get_transaction_history(self):
        return self.__transaction_history.copy()

    def display_wallet_info(self):
        print(f"Wallet ID: {self.wallet_id}")
        print(f"Owner Name: {self.owner_name}")
        print(f"Balance: {self.get_balance()}")

    #chunk 3: wallet operations
    def deposit(self, amount):
        if amount <= 0:
            print(f"Deposit of {amount} is zero or negative. Don't be silly!")
        else:
            self.__balance += amount
            self.__transaction_history.append(f"Transaction ID: {self.__transaction_id}, Previous Balance: {self.__balance - amount}, Deposit: {amount}, New Balance: {self.__balance}")
            self.__transaction_id += 1
            print(f"Successfully deposited {amount}. {self.__transaction_history[-1]}")
    
    def withdraw(self, amount):
        if amount <= 0:
            print(f"Withdrawal of {amount} is zero or negative. Shararti!")
        elif amount > self.__balance:
            print(f"Insufficient funds to withdrawal {amount}. Current balance: {self.__balance} Try again shararti")
        else:
            self.__balance -= amount
            self.__transaction_history.append(f"Transaction ID: {self.__transaction_id}, Previous Balance: {self.__balance + amount}, Withdrawal: {amount}, New Balance: {self.__balance}")
            self.__transaction_id += 1
            print(f"Successfully withdrew {amount}. {self.__transaction_history[-1]}")

w = Digital_Wallet("W123", "Alice", 1000)

w.deposit(500)
print(w.get_balance())               # 1500

w.withdraw(200)
print(w.get_balance())               # 1300

w.withdraw(5000)                     # rejected: insufficient funds
w.withdraw(0)                        # rejected: invalid amount
w.withdraw(-10)                      # rejected: invalid amount
print(w.get_balance())               # still 1300

w.withdraw(1300)                     # exact balance, should succeed
print(w.get_balance())               # 0

print(w.get_transaction_history())   # deposit, 2 withdrawals, no trace of rejected attempts