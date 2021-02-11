import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
print(con)
sql = con.cursor()
print(sql)
#create table;
sql.execute("use abcdb")
#"""create table table_name (column_name data_type(length),(column_name data_type(length),(column_name data_type(length),"""
def table_create(tb_name):
    query = "create table "+tb_name+"(id int primary  key," \
                                    "name varchar(30)," \
                                    "city varchar(30)," \
                                    "mobile int)"
    sql.execute(query)
    print("table created")
table_create("record")