class abc:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def getarea(self):
        print(self.l*self.b)
class xyz(abc):
    def __init__(self,s):
        self.s=s

    def getarea(self):
        print(self.s*self.s)
        s=self.s
        abc.__init__(self, s, s + 1)
        super().getarea()
p=xyz(50)
p.getarea()
