import mysql.connector
mydb = mysql.connector.connect(host="localhost",database="sona",user="root",passwd="root")
mycursor = mydb.cursor()
delete = "delete from sona where age=48"
mycursor.execute(delete)
mydb.commit()