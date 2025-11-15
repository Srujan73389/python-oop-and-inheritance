


class Student:
    def __init__(self,name,rollno,age):
        self.name=name  #public
        self._rollno=rollno  #protected
        self.__age=age   # private
    def __display(self):
        print(f"Hi myself {self.name} {self.__age} years old with rollno {self._rollno} from Student Class")
    def displayPrivateData(self):
        self.__display()

class Branch(Student):
    def show(self):
        print(f"My rollno is {self._rollno}")
s1=Student("Srujan",137,20)
# print(s1.__age)  # This Gives error bcz cant age to get private value directly
## We can access using public
s1.displayPrivateData()    ##We Will Get output

## another method is also there   by using name manly
s1._Student__display()      ##We Will Get output



