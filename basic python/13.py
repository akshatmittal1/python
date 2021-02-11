d1=dict()
d1={101:"akshat",102:"shubham"}
d2=dict()
d2={1001:["java",5,5],1002:["let us c",6,6]}
d3=dict()
i=103
j=1003
m=0
while(True):
    print("")
    print("-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-")
    print("1.add member")
    print("2.add books")
    print("3.borrow books")
    print("4.return books")
    print("5.member status")
    print("6.book status")
    print("7.quiet")
    n=int(input("enter choice"))
    if(n==1):
        a=input("enter name")
        d1.update({i:a})
        i=i+1
    if(n==2):
        b=input("enter book name")
        c=int(input("enter book quantiy"))
        m=c
        d=[b,c,m]
        d2.update({j:d})
        j=j+1
    if(n==3):
        p=int(input("enter member id"))
        if(p in d3):
            print("books alredy aloted")
        else:
            q=int(input("enter book id"))
            if(d2[q][1]>0):
                d3.update({p:q})
                d2[q][1]-=1
            else:
                print("book not available in stock")
    if(n==4):
        p=int(input("enter member id"))
        a=d3[p]
        d2[a][1]+=1
        del d3[p]
    if(n==5):
        p=int(input("enter member id"))
        print("member id-:",p)
        print("member name-:",d1[p])
        if(p in d3):
            print("book id issued-:",d3[p])
            a=d3[p]
            print("book name-:",d2[a][0])
        else:
            print("no book issued")
    if(n==6):
        p=int(input("enter book id"))
        print("book id-:",p)
        print("book name-:",d2[p][0])
        print("total no books-:",d2[p][2])
        a=d2[p][2]-d2[p][1]
        print("no of issued-:",a)
        print("no of books  in stock",d2[p][1])
        count=0
        for i in range(101,110):
            if(i in d3):
                if(d3[i]==p):
                    print("member id-:",i)
                    print("member name-:",d1[i])
                    count=1
        if(count==0):
            print("all books in stock")
    if(n==7):
        break

