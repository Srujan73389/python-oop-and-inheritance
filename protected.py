class Student:
    def __init__(self,name,marks):
        self.name=name
        self._marks=marks
    def _dis(self):
        print(f"Name : {self.name} , Marks : {self._marks}")
class op(Student):
    def se(self):
        self._dis()
s1=op("Srujan Kanaka",99)
s1.se()
s1._dis()