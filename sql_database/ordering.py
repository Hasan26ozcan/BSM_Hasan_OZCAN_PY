from typing import final
import mysql.connector

def getprotect():
    connect=mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )
    cursor=connect.cursor()
    cursor.execute("SELECT * FROM `node-app`.produtcs order by NAME,PRİCE DESC")# ASC normal az dan çoğa DESC çoktan aza
    # mesela burda büün hepsini seçtika am bir tanaesine göre sıralama yapmak istiyoruz o zaman order by diyerek
    # neye göre sıralamak istedigimizi yazıyoruz ve ona göre onu sıralıyoruz
    try:
        result=cursor.fetchall()
    # print(result)
        print(cursor)
        for i in result:
                print(i)
    except Exception as error:
        print(f"beklenmedik bir hatayla karşılaşıldır= {error} ")
    finally:
        connect.close()
        print("sistemimiz başarıyla kapatılmıştır ve degerlerimiz")

getprotect()
