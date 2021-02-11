import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
print(con)
sql = con.cursor()
print(sql)
#create database database_name;
def create_database(db_name):
    query="create database if not exists "+db_name
    print(query)
    sql.execute(query)
    print("database created")

create_database("abcdb")