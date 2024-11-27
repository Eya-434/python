class BankAccount:
    def __init__(self, int_rate=0.01, balance=0): 
        self.int_rate= int_rate
        self.balance=balance
    def make_deposit(self, amount):
        if amount>0 :
            self.balance+=amount
            print(f"Balance :{self.balance}")
    def make_withdraw(self, amount):
        if amount>0 and amount<= self.balance :
            self.balance-=amount
            print(f"Balance :{self.balance}")
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            print(f"Balace :{self.balance}")
    def display_account_info(self):
        print(f"Balance:{self.balance}")
    def yield_interest(self):
        if self.balance>0:
            self.balance+=(self.balance*self.int_rate)
            print(f"Balance+ Interest:{self.balance}")


class User:		
    def __init__(self,name , email ):
        self.name = name
        self.email = email
        self.account= BankAccount()

    def make_deposit(self, amount):
        print(f"User : {self.name}" , end="  ,   ")
        self.account.make_deposit(amount)
    
    def make_withdraw(self, amount):
        print(f"User : {self.name}" , end="  ,   ")
        self.account.make_withdraw(amount)

    def yiled_interest(self):
        print(f"User : {self.name}" , end="  ,   ")
        self.account.yield_interest()

    def display_account_info (self):
        print(f"User : {self.name}" , end="  ,   ")
        self.account.display_account_info()

    def transfert(self , other_user , amount):
        print(f"User : {self.name}" , end="  ,   ")
        self.account.make_withdraw(amount)
        print(f"User : {other_user.name}" , end="  ,   ")
        other_user.account.make_deposit(amount)

user1 = User("eya", "eya@gmail.com")
user2= User("ann","ann@gmail.com")
user1.display_account_info()
user1.make_deposit(100)
user1.make_withdraw(30)

user1.transfert(user2,30)
#user1.display_account_info()
#user2.display_account_info()