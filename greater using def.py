def big():
    a = int(input("a="))
    b = int(input("b="))
    c = int(input("c="))
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    else:
        return c
print("biggest",big())

