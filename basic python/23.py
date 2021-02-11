#truncate table tablename
#it is use to delete all data
import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
sql = con.cursor()
sql.execute("use abcdb")
id=int(input("enter id"))
sql.execute("delete from record where id = %d "%(id))
con.commit()