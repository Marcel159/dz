import mysql.connector 
mydb = mysql.connector.connect(
    host='localhost',
    user='root'
    password='55887799'
    database='test' 
)
mycursor = mydb.cursor()
mycursor.execute("create table tablle(id int,name VARCHAR(255))")
mycursor = mydb.cursor()
sql = "insert into tablle(id, name) values(%s, %s)"        
val = (1, "Star")
mycursor.execute (sql,val)
mydb.commit()
mycursor.execute("select * from tablle")
result = mycursor.fetchall()
print(result)
mycursor.execute("UPDATA 'table' set name = 'Mars' WEHER name = 'Star'" )
result = mycursor.fetchall()
mydb.commit()    