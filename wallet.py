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

    def Full_Transaction_History(self):
        if self.get_transaction_history() == []:
            print("No transactions have been made yet.")
        else:
            for transaction in self.get_transaction_history():
                print(f"Owner Name: {self.owner_name}, Wallet ID: {self.wallet_id} ")
                print(transaction)

carol = Digital_Wallet("W789", "Carol", 50)
carol.deposit(100)
carol.withdraw(30)
carol.Full_Transaction_History()