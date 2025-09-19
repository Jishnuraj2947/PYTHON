class stud:
    def __init__(self,a,b,c):
        self.sname=a
        self.sno=b
        self.sage=c
    def display(self):
        print("name:",self.sname)
        print("roll no:",self.sno)
        print("age:",self.sage)


class marks(stud):
    def __init__(self,a,b,c,m1,m2,m3):
        super(). __init__(a,b,c)
        self.mark1=m1
        self.mark2=m2
        self.mark3=m3
    def display(self):
        super().display()
        print("mark1:",self.mark1)
        print("mark2:",self.mark2)
        print("mark3:",self.mark3)


ob=marks("abc",2,18,45,55,46)
ob.display()