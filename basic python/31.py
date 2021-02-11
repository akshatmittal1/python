#overloading
class abc:
    def first(self,a=None):
        if a is not None:
            print("heloo "+a)
        else:
            print("heloo user")
obj=abc()
obj.first()
obj.first("akshat")