r=0
a=0
n=int(input("enter a no"))
s=n
while n > 0:
    r=n%10
    a=a*10+r
    n=n//10
if a==s:
    print("pallindrome")
else:
    print("not pallindrome")
    