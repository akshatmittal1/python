x=50
#global keyword
def fun1():
    global x
    x=10
    print(x)

def fun2():
    print(x)
def fun3():
#local keyword
    x=100
    print(x)
fun1()
fun2()
fun3()
