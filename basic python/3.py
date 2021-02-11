r=0
s=0
n=int(input("enter a no"))
while(n>0):
    r=n%10
    s=s+r
    n=n//10
print(s)