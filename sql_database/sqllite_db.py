import sqlite3

connected=sqlite3.connect("chinook.db")# eger varsa alır yoksa eger oluşturur bir veri tabanını

cursor=connected.cursor()
cursor.execute("select * from customers")
result=cursor.fetchall()
for i in result:
    print(i)
connected.commit()
connected.close()
