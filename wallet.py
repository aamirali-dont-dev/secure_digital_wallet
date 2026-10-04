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

tw = Digital_Wallet("W123", "Alice", 1000)

test = tw.get_transaction_history()
test.append("Test Transaction")

print(tw.get_transaction_history())
