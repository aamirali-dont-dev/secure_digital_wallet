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
        return f"Wallet ID: {self.wallet_id}, Owner Name: {self.owner_name}, Balance: {self.get_balance()}"

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
        elif not isinstance(receiver_wallet, Digital_Wallet):
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
            for transaction in self.get_transaction_history():
                print(f"Owner Name: {self.owner_name}, Wallet ID: {self.wallet_id} ")
                print(transaction)

test_ob1 = Digital_Wallet("001", "Saboor", 1000)
test_ob2 = Digital_Wallet("002", "Ali", 500)
test_ob3 = Digital_Wallet("003", "Danika", 2000)

# chunk 6: building a dictionary for easy search by wallet_id
wallets = {"001": test_ob1, "002": test_ob2, "003": test_ob3}

# loop to display all wallets and their balances
def display_all_wallets():
    for x in wallets:
        wallets[x].display_wallet_info()

# a search by ID function
def search_walletid(wallet_id):
    if wallet_id in wallets:
        print("Wallet Found!")
        print(f"{wallets[wallet_id].display_wallet_info()}")
    else:
        print(f"Wallet ID {wallet_id} does not exist. Buffoon!")

search_walletid("002")