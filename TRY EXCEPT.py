try:
    n=int(input("enter a number"))
    res=100/n
except ZeroDivisionError:
    print("you cant divide a number with Zero")
except ValueError:
    print("ENTER A VALID NUMBER")
else:
    print("result",res)
finally:
    print("execution completed")