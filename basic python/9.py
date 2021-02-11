d1={'a':100,'b':200}
d2={'x':1000,'y':2000,'a':200}
d1.update(d2)
print(d1)
k=input("enter key")
v=input("enter value")
d1.update({k:v})
del d1["y"]
print(d1)
