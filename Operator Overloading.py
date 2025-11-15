# print(1+2)    #3
# print("1"+"2")    #12
# print(int.__add__(2,3))   #5
# print(str.__add__("2","3"))   #23
class ComplexNUmber:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def __add__(self, other):
        return f"{self.real+other.real} + {self.imaginary+other.imaginary}i"
    def __sub__(self, other):
        return f"{self.real - other.real} - {self.imaginary - other.imaginary}i"



c1=ComplexNUmber(2,3)
c2=ComplexNUmber(5,8)
print(c1+c2)
print(c1-c2)

