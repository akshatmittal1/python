def fun1():
    print("helloo")
def fun2(a,b):
    print(a+b)


def fun3(a, b):
    print(a + b)
    return a+b
fun1()
fun2(50,60)
x=fun3(10,20)
print(x)


def fun4(*n):
    for i in n:
        print(i)


fun4(10,10,20,30)
#dictinory
def fun5(**n):
    print(n.keys())
    print(n.values())
fun5(name="akshat")



