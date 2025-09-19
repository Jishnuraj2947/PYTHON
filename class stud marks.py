from importlib.metadata import pass_none
from stringprep import map_table_b3, map_table_b2
from unittest.result import failfast


class stud:
    def __init__(self,a,b,c,m1,m2,m3):
        self.sname=a
        self.sno=b
        self.age=c
        self.mark1=m1
        self.mark2=m2
        self.mark3=m3

    def calulate(self):
        self.t=self.mark1+self.mark2+self.mark3
        self.avg=self.t/3
        print("total=:", self.t)
        print("average=:", self.avg)

        if m1>=35 and m2>=35 and m3>=35:
            self.result="passed"
        else:
            self.result="failed"
        print(self.result)

    def display(self):
            print("name:",self.sname)
            print("roll no:",self.sno)
            print("age:",self.age)
            print("mark1:",self.mark1)
            print("mark2:",self.mark2)
            print("mark3:",self.mark3)

x=input("enter your name: ")
y=input("roll: ")
z=int(input("enter your age: "))
m1=int(input("enter your mark1: "))
m2=int(input("enter your mark2: "))
m3=int(input("enter your mark3: "))

ob=stud(x,y,z,m1,m2,m3)
ob.display()
ob.calulate()