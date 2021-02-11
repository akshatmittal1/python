d1=dict()
d2=dict()
d3=dict()
i=101
j=1001
z=0
while(True):
    print("1.add member")
    print("2.add books")
    print("3.borrow books")
    print("4.return books")
    print("5.member status")
    print("6.book status")
    print("7.quiet")
    n=int(input())
    if(n==1):
        a=input("enter name")
        x=[a,z]
        d1.update({i:x})
        i=i+1
    if(n==2):
        b=input("enter book name")
        c=int(input("enter book quantiy"))
        d=[b,c]
        d2.update({j:d})
        j=j+1
    if(n==3):
        p=int(input("enter member id"))
        if(d1[p][1]==1):
            print("book alredy alloted")
        else:
            d1[p][1]=1
            q=int(input("enter book id"))
            d2[q][1]-=1
            d3.update({p:q})
    if(n==4):
        p = int(input("enter member id"))
        q = int(input("enter book id"))
        d2[q][1] += 1
        d1[p][1] = 0
    if(n==5):
        p=int(input("enter member id"))
        print("member id"+p)
        print("name"+d1[p][0])
        if (p in d[p]):
            a=d3[p]
            print(d2[a])







