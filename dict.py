d={"eno":123,"Ename":"abc"}
print(d)
print(d["eno"])
print(d["Ename"])
d["Ename"]="xyz"
print(d)
d["age"]=19
print(d)
for key in d:
    print(key)
for value in d.items():
    print(value)
for key,value in d.items():
    print(key,":",value)
d.pop("eno")
print(d)
d.popitem()
print(d)
d.clear()
print(d)