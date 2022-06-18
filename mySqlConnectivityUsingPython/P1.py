import mysql.connector
mydb = mysql.connector.connect(host="127.0.0.1" ,  database = "quastech" , user = "root" , passwd = "root")

mycursor = mydb.cursor()
mycursor.execute("SHOW databases")

for db in mycursor:
    print(db)

