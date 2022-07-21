import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql1234",
    database="MYDATABASE"
    )

print(mydb)
# eger mysql worbeach yoksa ya indirmiyorsak o zaman şununlada bbiz kendimize bir database oluşturabiliriz


mycursor=mydb.cursor() 
# mycursor.execute("CREATE DATABASE MYDATABASE")

mycursor.execute("SHOW DATABASES")

for i in mycursor:
    print(i)

#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), adress VARCHAR(255) )")


