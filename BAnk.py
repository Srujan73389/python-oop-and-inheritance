class Money:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amt):
        self.__balance+=amt
        print(f"Deposited Money: {amt} and Balance : {self.__balance}")
    def withdr(self,amm):
        if amm<self.__balance:
            self.__balance-=amm
            print(f"Withdraw :{amm},Balance : {self.__balance}")

m1=Money(1000)
m1.deposit(500)
m1.withdr(600)