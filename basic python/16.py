#non local keyword
def fun1():
    x=10
    def fun2():
        nonlocal x
        x=50
        def fun3():
            nonlocal x
            x=20
            print(x)
        fun3()

        print(x)
    fun2()
    print(x)
fun1()