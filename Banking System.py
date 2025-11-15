def menu():
    print("---BANKING SYSTEM---")
    print("1.Check Balance")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Exit")
balance=0
while(True):
    menu()
    choice=int(input("Enter Your Choice:"))
    if choice==1:
        print("Balance is : ",balance)
    if choice==2:
        amt=int(input("Enter amount to deposit:"))
        print("Deposited Money is : ",amt)
        balance+=amt
    if choice==3:
        amt = int(input("Enter amount to withdraw:"))
        if amt<balance:
            balance-=amt
        else:
            print("Insufficiant Balance")
    if choice==4:
        print("Thank You ")
        break