class University:
    def __init__(self,uni_name):
        self.uni_name=uni_name
    def display(self):
        print(f"University: {self.uni_name}")
class Course(University):
    def __init__(self,cou_name,uni_name):
        self.cou_name=cou_name
        University.__init__(self,uni_name)
    def display(self):
        print(f"Course Name: {self.cou_name}")

class Branch(University):
    def __init__(self,br_name,uni_name):

        University.__init__(self,uni_name)
        self.br_name = br_name

    def  display(self):
        print(f"Branch Name: {self.br_name}")
        print(f"University: {self.uni_name}")

class Student(Course,Branch):
    def __init__(self,s_name,br_name,uni_name,cou_name):
        self.s_name=s_name
        University.__init__(self, uni_name)
        Course.__init__(self,cou_name,uni_name)
        Branch.__init__(self,br_name,uni_name)

    def display(self):
        print(f"Student Name: {self.s_name}")
        print(f"Branch Name: {self.br_name}")
        print(f"University: {self.uni_name}")
        print(f"Course Name: {self.cou_name}")
class Faculty(Branch):
    def __init__(self,f_name,br_name,uni_name):
        University.__init__(self, uni_name)

        Branch.__init__(self, br_name,uni_name)
        self.f_name=f_name
    def display(self):
        print(f"Facuty name :{self.f_name}")
        print(f"Branch Name: {self.br_name}")
        print(f"University: {self.uni_name}")
d=Faculty("SRUJAN KANAKA","CSE","RAMAIAH")
d.display()

