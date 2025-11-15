class Student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def get_name(self):         #GETTER METHOD
        return self.__name
    def get_age(self):         #GETTER METHOD
        return self.__age
    def set_name(self,name):     #SETTER METHOD
        self.__name=name
    def set_age(self,age):            #SETTER METHOD
        if isinstance(age,int):
            self.__age=age
        else:
            print("give an int type")
s=Student("Srujan",20)
print(f"Before Name : {s.get_name()}")
s.set_name("SRUJAN KAKANA")
print(f"After Name : {s.get_name()}")
print(f"Before Age : {s.get_age()}")
s.set_age(22)
print(f"After Age : {s.get_age()}")

