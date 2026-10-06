# chunk 1: class creation and encapsulation
class DigitalWallet:
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

    def display_wallet(self):
        print(f"Wallet ID: {self.wallet_id}")
        print(f"Owner Name: {self.owner_name}")
        print(f"Balance: {self.get_balance()}")

    #chunk 3: wallet operations
    def deposit(self, amount):
        if amount <= 0:
            print(f"Deposit of {amount} is not allowed. It's zero or negative. Don't be silly!")
        else:
            self.__balance += amount
            self.__transaction_history.append(f"Transaction ID: {self.__transaction_id}, Nature: Cr, Previous Balance: {self.__balance - amount}, Deposit: {amount}, New Balance: {self.__balance}")
            print(f"Successfully deposited {amount}. {self.__transaction_history[-1]}")
            self.__transaction_id += 1
            return True
        return False

    def withdraw(self, amount):
        if amount <= 0:
            print(f"Withdrawal of {amount} is not allowed. It's zero or negative. Shararti!")
        elif amount > self.__balance:
            print(f"Insufficient funds to withdrawal {amount}. Current balance: {self.__balance} Try again shararti")
        else:
            self.__balance -= amount
            self.__transaction_history.append(f"Transaction ID: {self.__transaction_id}, Nature: Dr, Previous Balance: {self.__balance + amount}, Withdrawal: {amount}, New Balance: {self.__balance}")
            print(f"Successfully withdrew {amount}. {self.__transaction_history[-1]}")
            self.__transaction_id += 1
            return True
        return False
    
    def transfer(self, amount, receiver_wallet):
        if amount <= 0:
            print(f"Transfer of {amount} is not allowed. It's zero or negative. Shararti!")
            return False
        elif not isinstance(receiver_wallet, DigitalWallet):
            print("Receiver wallet does not exist. Shararti!")
            return False
        elif receiver_wallet == self:
            print("Cannot transfer to the same wallet. Shararti!")
            return False
        elif amount > self.__balance:
            print(f"Insufficient funds to transfer {amount}. Current balance: {self.__balance} Try again shararti")
            return False
        else:
            self.__balance -= amount
            self.__transaction_history.append(f"Transaction ID: {self.__transaction_id}, Nature: Dr, Previous Balance: {self.__balance + amount}, Transfer to Wallet ID: {receiver_wallet.wallet_id}, Amount: {amount}, New Balance: {self.__balance}")
            self.__transaction_id += 1
            receiver_wallet.__balance += amount
            receiver_wallet.__transaction_history.append(f"Transaction ID: {receiver_wallet.__transaction_id}, Nature: Cr, Previous Balance: {receiver_wallet.__balance - amount}, Transfer from Wallet ID: {self.wallet_id}, Amount: {amount}, New Balance: {receiver_wallet.__balance}")
            receiver_wallet.__transaction_id += 1
            print(f"Successfully transferred {amount} to {receiver_wallet.owner_name}")
            return True

    # chunk 5: full transaction history using public method for security reasons
    def Full_Transaction_History(self):
        if self.get_transaction_history() == []:
            print("No transactions have been made yet.")
        else:
            print("Here's the full transaction history of your wallet:")
            print(f"Owner Name: {self.owner_name}, Wallet ID: {self.wallet_id}")
            for transaction in self.get_transaction_history():
                print(transaction)

# Manual objects for use in dictionary
test_ob1 = DigitalWallet("001", "Saboor", 1000)
test_ob2 = DigitalWallet("002", "Ali", 500)
test_ob3 = DigitalWallet("003", "Danika", 2000)

# chunk 6: building a dictionary for easy search by wallet_id
wallets = {"001": test_ob1, "002": test_ob2, "003": test_ob3}

# loop to display all wallets and their balances
def display_all_wallets():
    for x in wallets:
        wallets[x].display_wallet()

# a search by ID function
def search_walletid(wallet_id):
    if wallet_id in wallets:
        print("Wallet Found!")
        wallets[wallet_id].display_wallet()
    else:
        print(f"Wallet ID {wallet_id} does not exist. Buffoon!")

# chunk 7: test cases
print("1. Starting state")
display_all_wallets()                      # 001: 1000, 002: 500, 003: 2000

print("\n 2. Deposit")
test_ob1.deposit(500)                      # success -> 001 = 1500
print("\n Rejected deposits ")
test_ob1.deposit(0)                        # rejected
test_ob1.deposit(-20)                      # rejected
print("001 balance:", test_ob1.get_balance())   # still 1500

print("\n 3. Withdraw")
test_ob2.withdraw(200)                     # success -> 002 = 300
print("\nRejected withdrawals")
test_ob2.withdraw(5000)                    # rejected: insufficient funds
test_ob2.withdraw(0)                       # rejected: zero
test_ob2.withdraw(-10)                     # rejected: negative
print("002 balance:", test_ob2.get_balance())   # still 300

print("\n 4. Transfer")
test_ob1.transfer(300, test_ob3)           # success -> 001 = 1200, 003 = 2300
print("\n Rejected transfers ")
test_ob2.transfer(5000, test_ob1)          # rejected: insufficient funds
test_ob1.transfer(0, test_ob3)             # rejected: zero
test_ob1.transfer(-50, test_ob3)           # rejected: negative
test_ob1.transfer(100, test_ob1)           # rejected: same wallet
test_ob1.transfer(100, "999")              # rejected: not a wallet
print("001 balance:", test_ob1.get_balance())   # still 1200
print("003 balance:", test_ob3.get_balance())   # still 2300

print("\n 5. Boundary: withdraw the exact balance")
test_ob2.withdraw(300)                     # success -> 002 = 0

print("\n 6. Search")
search_walletid("002")                     # found
search_walletid("999")                     # not found, no crash

print("\n 7. Encapsulation")
#print(test_ob1.__balance)              # must NOT work

history = test_ob1.get_transaction_history()
history.append("hacked entry")             # tamper with the copy
print("Original history length:", len(test_ob1.get_transaction_history()))  # still 2

print("\n 8. Constructor validation / empty history")
bad = DigitalWallet("004", "Kainat", -50)    # warning, balance set to 0
print("004 balance:", bad.get_balance())   # 0
bad.Full_Transaction_History()             # "No transactions have been made yet."

print("\n 9. Transaction histories")
test_ob1.Full_Transaction_History()        # 2 records: IDs 1 and 2
test_ob2.Full_Transaction_History()        # 2 records: IDs 1 and 2
test_ob3.Full_Transaction_History()        # 1 record: ID 1

print("\n 10. Final balances")
display_all_wallets()                      # 001: 1200, 002: 0, 003: 2300

