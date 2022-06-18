import mysql.connector
mydb = mysql.connector.connect(host="localhost",database="sona",user="root",passwd="root")
mycursor = mydb.cursor()
update = "update sona set age=48"
mycursor.execute(update)
mydb.commit()
