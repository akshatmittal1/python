l=list()
i=0
while(i<5):
    n=int(input("enter a no"))
    if(n in l ):
        print("duplicate")
    else:
        l.insert(i,n)
        i=i+1