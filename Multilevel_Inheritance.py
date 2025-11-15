class Human:
    dooo=True
    def __init__(self,heart):
        self.no_eyes=1
        self.heart=heart
    def eat(self):
        print("I can eat")

    def work(self):
        print("I can work")
class Male(Human):
    def __init__(self,name):
        self.name=name
    def sleep(self):
        print("I can sleep")
class Boy(Male):
    def __init__(self,heart,name,hr):
        Male.__init__(self,name)
        Human.__init__(self,heart)
        self.hr=hr
    def work(self):
        super().work()
        print("I can code")
b1=Boy(1,"bsjb",True)
print(b1.heart)
b1.work()
print(b1.dooo)

