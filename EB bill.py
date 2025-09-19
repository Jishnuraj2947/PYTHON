class eb:
    def __init__(self,a,b,c,d,e,u1):
        self.name=a
        self.cno=b
        self.add=c
        self.unit=d
        self.pre=e
        self.amt=u1

    def calculate(self):
        self.bill=(self.unit-self.pre)*self.amt

    def display(self):
        print("name:",self.name)
        print("consumer number:",self.cno)
        print("address",self.add)
        print("unit consumed:",self.unit)
        print("previous:",self.pre)
        print("bill:",self.bill,"rs")
        print("amount per unit:",self.amt)

x=input("enter your name:")
y=input("enter your consumer number:")
z=input("enter your address:")
u=int(input("enter your unit consumed:"))
p=int(input("enter your previous unit consumed:"))
u1=int(input("amount per unit:"))

ob=eb(x,y,z,u,p,u1)
ob.calculate()
ob.display()


