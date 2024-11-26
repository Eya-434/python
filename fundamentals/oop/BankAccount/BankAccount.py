class BankAccount:
    def __init__(self, int_rate=0.01, balance=0): 
        self.int_rate= int_rate
        self.balance=balance
    def deposit(self, amount):
        if amount>0 :
            self.balance+=amount
            print(f"Balance :{self.balance}")
        else: print("")
    def withdraw(self, amount):
        if amount>0 and amount<= self.balance :
            self.balance-=amount
            print(f"Balance :{self.balance}")
        else: print("Insufficient funds: Charging a $5 fee")
        self.balance-=5
    def display_account_info(self):
        print(f"Balance:{self.balance}")
    def yield_interest(self):
        if self.balance>0:
            interest = self.balance*self.int_rate
            self.balance+=interest
            print(f"Balance+ Interest:{self.balance}")

account1= BankAccount(0.02, 1000)
account2= BankAccount(0.03,5000)
