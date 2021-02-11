import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
sql = con.cursor()
sql.execute("use abcdb")
a=int(input("enter id"))
b=input("enter name")
c=input("enter city name")
d=int(input("enter mobile no"))
qry="insert into record values(%d,'%s','%s',%d)"%(a,b,c,d)

print(qry)
sql.execute(qry)
con.commit()