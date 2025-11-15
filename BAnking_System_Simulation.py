class Account:
    def __init__(self,id,holdername):
        self.id=id
        self.holdername=holdername
        self._balance=0
    def check_balance(self):
        print("Balance:",self._balance)
    def deposit(self,amount):
        self._balance+=amount
        print(f"Deposited Successfully. Updated Balance : {self._balance}")
    def withdraw(self,amount):
        if amount<self._balance:
            self._balance-=amount
            print(f"Withdraw Successfully. Updated Balance : {self._balance}")
        else:
            print("Insufficient Balance!!")
class Savings_Account(Account):
    def calculateinterest(self):
        INTEREST=0.04
        inter=self._balance*INTEREST
        print("INTEREST IS : ",inter)
class Current_Account(Account):
    def withdraw(self,amount):
        OVERDRAFT_LIMT=1000
        if amount<self._balance+OVERDRAFT_LIMT:
            self._balance-=amount
            print(f"Withdraw Successfully. Updated Balance : {self._balance}")
        else:
            print("Asked over limit!!")

class Bank:
    def __init__(self,name,city):
        self.name=name
        self.city=city
        self.__account={}
    def crete_account(self,id,holdername,type):
        if type=="savings":
            new_account=Savings_Account(id,holdername)
        elif type=="current":
            new_account=Current_Account(id,holdername)
        self.__account[id]=new_account
        print("cretaed")
        return new_account

c=Bank("Srujan bank of karnataak","Chikkamagalur")
s1=c.crete_account("1","Darshan","savings")
s2=c.crete_account("2","KANAKA","current")
s1.deposit(1000)
s1.withdraw(200)
s2.deposit(2000)
s2.withdraw(2300)
s1.calculateinterest()
s2.check_balance()
