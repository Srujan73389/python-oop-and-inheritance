from abc import ABC , abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def startengine(self):
        pass
class Car(Vehicle):
    def __init__(self,name):
        self.name=name
    def startengine(self):
        print("Hello")
c=Car("KTM")
print(c.name)
c.startengine()
