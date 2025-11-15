class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def ShowDetails(self):
        print(f"Name : {self.name} , Age : {self.age}")
    def eat(self):
        print("I can Eat")
class Male(Human):
    def __init__(self,name,age,location):
        super().__init__(name,age)
        self.location=location
    def sleep(self):
        print("I can Sleep!")
class Female(Human):
    def __init__(self,name,age,can):
        super().__init__(name,age)
        self.can=can
    def show(self):
        Human.ShowDetails(self)
        print(f"Can : {self.can}")
    def work(self):
        print("I can work")
f=Female("Srujan Kanaka",200,True)
print(f.age)
f.show()
m=Male("kuruba",73,"wdig")
print(m.name)
f.ShowDetails()

