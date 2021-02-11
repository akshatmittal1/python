#it is use to fetch a data
import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
sql = con.cursor()
sql.execute("use abcdb")
qry="select * from record"
sql.execute(qry)
data=sql.fetchall()
print(data[0][0])
for i in range(0,3):
    for j in range(0,4):
        print(data[i][j])
print(data)
for i in data:
    print(i)