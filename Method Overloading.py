class Calculator:
    def __init__(self,a,b,c=0):     #  we are using default Parameter
        print(a+b+c)
c=Calculator(1,2,3)
c=Calculator(1,2)


## Using *args

class Calci:
    def __init__(self,*args):
        total=0
        for i in args:
            total+=i
        print(total)
c=Calci(2,3)
c=Calci(2,3,4,5)