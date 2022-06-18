import mysql.connector
mydb = mysql.connector.connect(host="localhost", database ="sona", user="root" , passwd="root")
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for table in mycursor:
    print(table)
