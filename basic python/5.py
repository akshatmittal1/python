c=0
n=int(input("enter a no"))
for i in range (2,n-1):
   if(n%i==0):
        c=1
        break
if(c==1):
    print("its not prime no")
else:
    print("its prime no")