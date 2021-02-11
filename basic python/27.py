print("heloo, i am in a file")
def sum():
    print("sum function")
    print(__name__)
if(__name__=="__main__"):
    print("restricted code" )
    #if module use this code then it cannot access restrictrd code