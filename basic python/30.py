class abc:
    def first(self):
        print("first")
class xyz(abc):
    def second(self):
        print("second")
obj=xyz()
obj.first()
obj.second()
