def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def disp():
    print("##SIMPLE CALCULATOR::")
    print(" 1. ADDITION\n2. SUBTRACTION\n3. MULTIPLICATION\n4. DIVISION\n 5. QUIT")

while(True):
    disp()


    choice=int(input("ENTER YOUR CHOICE:"))
    if choice in {1,2,3,4}:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))

    if choice==1:
        print("Result : ",add(a,b))
    elif choice==2:
        print("Result : ",sub(a,b))
    elif choice==3:
        print("Result : ",mul(a,b))
    elif choice==4:
        print("Result : ",div(a,b))

    elif choice== 5:
        print("QUITTING")
        break
    else:
        print("Try again")




