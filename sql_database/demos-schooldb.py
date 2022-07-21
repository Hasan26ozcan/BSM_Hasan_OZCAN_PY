from turtle import pen
from connection import connect
import datetime
import mysql.connector


class student:
    connec=connect
    cursor=connec.cursor()
    connec=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql1234",
    database="schooldb"
)
    
    @staticmethod
    def savemanystudents():
        student.cursor.execute("SELECT * FROM schooldb.student")
        result=student.cursor.fetchall()
        for i in result:
            print(i)
    @staticmethod
    def namenumbersurname():
        student.cursor.execute("SELECT studentnumber,name,surname FROM schooldb.student")
        result=student.cursor.fetchall()
        for i in result:
            print(f"studentnumber={i[0]} name={i[1]} surname={i[2]}  ")
    @staticmethod
    def girlnamesurname():
        student.cursor.execute("SELECT name,surname FROM schooldb.student where gender='K' ")
        result=student.cursor.fetchall()
        for i in result:
            print(f" NAME={i[0]}  SURNAME={i[1]}  ")
    @staticmethod
    def countman():
        student.cursor.execute("SELECT count(*) FROM schooldb.student where gender='E'")
        result=student.cursor.fetchall()
        print(result)
        for i in result:
            print(i)
    def birth2003():
        sql=("select * from schooldb.student where year(birhdate) = 2003")
        student.cursor.execute(sql)
        result=student.cursor.fetchall()
        for i in result:
            print(i)
    def ali2005():
        student.cursor.execute("select* from schooldb.student where name='Ali' and year(birhdate)=2005 ")
        result=student.cursor.fetchall()
        print(result)
        for i in result:
            print(i)
    def namesurnameinan():
        student.cursor.execute("select * from schooldb.student where name LIKE '%an% ' or surname like '%an%'  ")
        result=student.cursor.fetchall()
        print(result)
        for i in result:
            print(i)
    def sortgirl():
        student.cursor.execute("SELECT * FROM schooldb.student where gender='K' order by name ")
        result=student.cursor.fetchall()
        print(result)
        for i in result:
            print(i)
    def firstfivesave():
        student.cursor.execute("SELECT * FROM schooldb.student limit 5")
        result=student.cursor.fetchall()
        for i in result:
            print(i)



#4- Aşağıdaki sorguları yazınız
#   a- tüm öğrencilerin kayıtlarını alınız
print("**")
student.savemanystudents()
print("**")
#   b-tüm ogrencilerin sadece ogrenci no,ad ve soyad bilgilerini alınız

print("**")
student.namenumbersurname()
print("**")


#   c- sadece kız ogrencilerin ad ve soyadlarını alınız
print("**")
student.girlnamesurname()

print("**")


#   d- 2003 dogumlu ogrenci bilgilerini alınız
print("**")
student.birth2003()
print("**")
#   e- ismi ali ve dogum tarihi 2005 olan ogrenci bilgilerini alınız
print("**")
student.ali2005()
print("**")
#   f- ad ve ya soyadı içinde an ifadesi geçen kayıtları alınız
print("**")
student.namesurnameinan()
print("**")
#   g- kaç erkek ogrenci vardır
print("**")
student.countman()
print("**")
#   h- kız ogrencileri harf sırasına göre getiriniz
print("**")
student.sortgirl()
print("**")

# fetch the first 5 records

student.firstfivesave()