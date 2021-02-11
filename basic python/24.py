#update query

import mysql.connector
con =mysql.connector.connect(
    host="localhost",
    user="root",
    password = ""

)
sql = con.cursor()
sql.execute("use abcdb")
c="kkk"
d=123
qry = "update record set city='%s' where id=%d"%(c,d)
sql.execute(qry)
con.commit()

