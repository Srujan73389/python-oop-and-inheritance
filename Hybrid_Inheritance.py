class A:
    def display(self):
        print("Display from class A")
class B(A):
    def display(self):
        print("Display from class B")
class C:
    def show(self):
        print("HI! from class C")
class D(B,C):
    def display(self):
        A.display(self)
        print("Display from class D")
d=D()
d.display()
