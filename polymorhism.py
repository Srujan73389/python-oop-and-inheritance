class Shape:
    pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def calculateArea(self):
        print(f"Area of circle : {3 * self.radius *self.radius}")
class Rectangle(Shape):
    def __init__(self,len,bre):
        self.len=len
        self.bre=bre
    def calculateArea(self):
        print(f"Area of rectangle : {self.len * self.bre}")

c=Circle(2)
r=Rectangle(4,5)
shape=[c,r]
for i in shape:
    area=i.calculateArea()

#
# c.calculateArea()
# r.calculateArea()