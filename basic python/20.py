#dml function create,update,delete and use commit function
import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
sql = con.cursor()
sql.execute("use abcdb")
qry="insert into record values(123,'abc','xyz',345)"
sql.execute(qry)
con.commit()