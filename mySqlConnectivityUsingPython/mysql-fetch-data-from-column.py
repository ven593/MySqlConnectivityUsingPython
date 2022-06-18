import mysql.connector
mydb = mysql.connector.connect(host="localhost",database="sona",user="root",passwd="root")
mycursor = mydb.cursor()
mycursor.execute("select * from sona")
result = mycursor.fetchall()
for i in result:
    print(i)