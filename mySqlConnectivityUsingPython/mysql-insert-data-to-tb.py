import mysql.connector
mydb = mysql.connector.connect(host="localhost",database="sona",user="root",passwd="root")

#sqlform = "insert into sona(age,name) values(%s,%s)"
#data = [(16,"abc"),(17,"xyz"),(18,"pqr")]
mycursor = mydb.cursor()
#mycursor.executemany(sqlform,data)
#mydb.commit()
mycursor.execute("select* from sona")
for i in mycursor:
    print(i)
