from cgitb import reset
import dbm
import mysql.connector
from datetime import datetime
from connection import connect
from student import student
from teacher import teacher
from Class import Class

class dbmanager:
    def __init__(self):
        self.connection=connect
        self.cursor=self.connection.cursor()

    def getstudentbyıd(self,id):
        sql="select * from schooldb.student where id=%s "
        values=(id,)
        self.cursor.execute(sql,values)
        try:
            result=self.cursor.fetchone()
            print(result)
            return student.createstudent(result)
        except Exception as err:
            print(f"hata {err} ")

    def getstudentbyclassıd(self,classıd):
        sql="select * from schooldb.student where classıd=%s"
        values=(classıd,)
        self.cursor.execute(sql,values)
        try:
            result=self.cursor.fetchall()
            print(result)
            return student.createstudent(result)
        except Exception as err:
            print(f"hata {err} ")



    def addstudentoreditstudent(self,student:student):
        if(student.id==None):
            dbmanager.addstudent(student=student)
        else:
            dbmanager.editstudent(student=student)



    def addstudent(self,student:student):# burda gelicek olan şeyin tipinin ne odlugunu yazıyoruz
        sql=("INSERT INTO `schooldb`.`student` (`studentnumber`, `name`, `surname`, `birhdate`, `gender`,classıd) VALUES (%s,%s,%s,%s,%s,%s)")
        value=(student.studentnumber,student.name,student.surname,student.birhdate,student.gender,student.classid)
        self.cursor.execute(sql,value)
        dbmanager.commitcontrol(self)
        
    def commitcontrol(self):    
        try:
            connect.commit()# aslında connectionu böylede kullanabiliriz aşağıda close oldugu yerde oldugu gibide
            print(f" {self.cursor.rowcount} tane satır eklenmistir ")
            print(f" son kaydın ıd si {self.cursor.lastrowid} ")
        except Exception as error :
            print(f"Hata {error} ")
        else:
            print("islem basarıyla gerceklesti")
        finally:
            connect.close()
    def editstudent(self,student:student):
        sql="UPDATE `schooldb`.`student` SET `name`=%s,surname=%s,gender=%s,classıd=%s WHERE (`id` = %s)"
        values=(student.name,student.surname,student.gender,student.classid,student.id)
        self.cursor.execute(sql,values)
        try:
            connect.commit()
            print(f" {self.cursor.rowcount} tane kayıt güncellenmiştir ")
        except Exception as err:
            print(f"HATA  {err} ")
        finally:
            connect.close()
            print("işlem başarılı bir şekilde yapılmıştır")
    # def __del__(self):
    #     connect.close()
    #     print("sistem başarıyla kapanmıştır")

    def getclassed(self):
        sql="select * from schooldb.class"
        self.cursor.execute(sql)
        try:
            result=self.cursor.fetchall()
            print(result)
            return Class.createclass(result)
        except Exception as err:
            print(f"hata {err} ")
    def deletestudent(self,id):# burda gelicek olan şeyin tipinin ne odlugunu yazıyoruz
        sql="DELETE FROM `schooldb`.`student` WHERE (`id` = %s)"
        values=(id,)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
        except Exception as err:
            print("hata",err)
        finally:
            print("işlem başarıyla tamamlanmıştır")
             
# a=dbmanager(connection=connect)

# obj=a.getstudentbyıd(6)

# print(obj[0].name)
# print(obj[0].surname)
# obj[0].studentnumber="1111"
# obj[0].name="çınar"
# obj[0].surname="eksik"

# a.editstudent(obj[0])




# obj=a.getstudentbyclassıd(1)
# order=[0,1,2,3,4,5,6]
# for i in order:
#     print(obj[i].name,obj[i].surname)
