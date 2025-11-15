class Vehicle:
    def start(self):
        print("Running")
class Bike(Vehicle):
    def ride(self):
        print("riding")
b=Bike()
b.ride()
b.start()