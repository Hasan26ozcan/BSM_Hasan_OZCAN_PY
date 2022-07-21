from sqlite3 import connect
from unittest import result
import mysql.connector


def getprotect():
    connect=mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )
    cursor=connect.cursor()
    sql="SELECT count(price) FROM `node-app`.produtcs"
    sql="SELECT avg(price) FROM `node-app`.produtcs"
    sql="SELECT sum(price) FROM `node-app`.produtcs"
    sql="SELECT max(price) FROM `node-app`.produtcs"
    sql="SELECT min(price) FROM `node-app`.produtcs"
    sql="SELECT name,price FROM `node-app`.produtcs where  price=(SELECT max(price) FROM `node-app`.produtcs) "
    # count orda eger koşulumuzda varsa kaç tanesağladı diye onu sayıyor
    # avg ise seçtiğimiz kolondaki sayıların ortalamasını alıyor
    # sum ise toplama islemini yerine getiriyor
    # max ise o sutundaki maximum degeri veriyor
    # min ise o sutundaki minimum degeri veriyor
    cursor.execute(sql)
    result=cursor.fetchall()
    print(result)

getprotect()
