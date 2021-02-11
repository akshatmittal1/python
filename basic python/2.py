l=list()
i=0
while(i<5):
    n=int(input("enter a no"))
    if(i%2==0):
        l.insert(i,n)
        i=i+1
    elif(n%2==0):
       print("even no on odd place not allowed")
    else:
        l.insert(i,n)
        i=i+1
print(l)