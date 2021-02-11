class abc:
    def __init__(self):
        self.a=10000
        self.b=20000
    def setvalue(self):
        self.a=400
        self.b=500
    def getvalue(self):
        print(self.a+self.b)
p=abc()
p.getvalue()
p.setvalue()
p.getvalue()