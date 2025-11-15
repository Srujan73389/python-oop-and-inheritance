class Human:
    def __init__(self,heart):
        self.no_of_eyes=2
        self.no_of_nose=1
        self.heart=heart

    def eat(self):
        print("I can Eat.")
    def work(self):
        print("I can Work!.")
class Male:
    def __init__(self,name):
        self.name=name

    def flirt(self):
        print("I can Flirt!.")

    def work(self):
        print("I can Code!.")
class Boy(Human,Male):
    def __init__(self,name,lang,heart):
        Male.__init__(self,name)     # need to use this
        Human.__init__(self,heart)
        self.lang=lang

    def sleep(self):
        print("I can sleep")
    def work(self):
        print("i may gooo")
b1=Boy('Srujan',2,4)
# b1.eat()   #I can Eat.
# b1.flirt() #I can Flirt!.
# b1.work()   #i may gooo
# # Male.work(b1)   # I can Code!.
# print(Boy.mro())
# print(b1.no_of_eyes)  #2
print(b1.no_of_nose)
print(b1.heart)