
import mysql.connector

def getprtodutcs():
    connect=mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )
    cursor=connect.cursor()
    cursor.execute("SELECT name,price FROM `node-app`.produtcs")
    #     cursor.execute("SELECT * FROM `node-app`.produtcs")




    # "*" yılzı ordaki bütün başlıkları sütun başlıklarının hepsini seçmesini saglıyor
    # eger yılzı yerine biz istediğimiz kolonların adlarını yazarsak o zaman 
    # istediklerimiz gelir ve büyük verilerde kolaylık sağlar
    # result=cursor.fetchall() böyleyken hepsini alır
    result=cursor.fetchone() # boöyleyken ise ilk satırı almamızı sağlar
    print(f"name: {result[0]} price: {result[1]} ")











##### döngü varken bu sistem işey yarar ama tek deger varken bu sistem işey yaramaz
    # print(result)
    # for i in result:
    #     print(f"name: {i[0]} price: {i[1]} ")


getprtodutcs()