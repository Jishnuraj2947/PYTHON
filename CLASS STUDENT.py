class stud:
    def __init__(self,a,b,c):
        self.sname=a
        self.sno=b
        self.age=c
    def display(self):
            print("name:",self.sname)
            print("roll no:",self.sno)
            print("age:",self.age)

x=input("enter your name")
y=input("roll")
z=int(input("enter your age"))

ob=stud(x,y,z)
ob.display()




