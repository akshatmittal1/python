import mysql.connector
con =mysql.connector.connect(
    host="localhost",
    user="root",
    password = ""

)
sql=con.cursor()
sql.execute("use abcdb")
h=0
print("1.signup")
print("2.login")
n=int(input("enter your choise"))
if(n==1):
    a=input("enter name")
    b=input("eneter email")
    c=input("enter password")
    d=input("enter city")
    e=int(input("enter mobile no"))
    qry = "insert into login values('%s','%s','%s','%s',%d)"%(a,b,c,d,e)
    sql.execute(qry)
    con.commit()
if(n==2):
    a=input("enter a email")

    qry = "select * from login"
    sql.execute(qry)
    data=sql.fetchall()
    l=len(data)
    #print("length",l)
    for i in range(0,l):
        if(a==data[i][1]):
            b = input("enter a password")
            h=1
            if(b==data[i][2]):
                print("login successful")
            else:
                print("password incorrect")
if(h==0):
    print("username is incorrect")


