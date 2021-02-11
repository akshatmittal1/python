r=0
s=0
n=int(input("enter a no"))
a=n
l=len(str(n))
print(l)
while(l>=0):
    r=n%10
    s=s+r**l
    n=n//10
    l=l-1
if(a==s):
    print("its amstrong")
else:
    print("its not armstrong no")

