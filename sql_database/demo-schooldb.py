# 1- workbench IDE ile schooldb isminde bir database oluşturup student tablosu
# ıd studentnumber , name, surname,birthdate,gender

# 2- database bağlantısı oluşturunuz

# 3- aşağıdaki bilgiler için inser sorguları oluşturup kayıtları ekleyiniz
import datetime
from connection import connect
ogrenci=[
      ("301","mehmet","yılmaz",datetime.datetime(2005,5,17),"E"),
      ("302","rahat","Can",datetime.datetime(2005,6,17),"E"),
      ("303","berna","Tan",datetime.datetime(2005,7,7),"k"),
      ("304","fulya","Tane",datetime.datetime(2005,9,23),"k"),
      ("305","sakarya","Toksöz",datetime.datetime(2004,7,27),"E"),
      ("306","fırat","Cenk",datetime.datetime(2003,8,25),"E")
]





class student:
    connect=connect
    cursor=connect.cursor()
    def __init__(self,studentnumber,name,surname,birhdate,gender):
        self.studentnumber=studentnumber
        self.name=name
        self.surname=surname
        self.birhdate=birhdate
        self.gender=gender


    def saveonestudent(self):
        sql=("INSERT INTO `schooldb`.`student` (`studentnumber`, `name`, `surname`, `birhdate`, `gender`) VALUES (%s, %s,%s,%s,%s)")
        student.cursor.execute(sql,(self.studentnumber,self.name,self.surname,self.birhdate,self.gender))
        student.commitcontrol(self)
        
    def commitcontrol(self):    
        try:
            student.connect.commit()# aslında connectionu böylede kullanabiliriz aşağıda close oldugu yerde oldugu gibide
            print(f" {student.cursor.rowcount} tane satır eklenmistir ")
            print(f" son kaydın ıd si {student.cursor.lastrowid} ")
        except Exception as error :
            print(f"Hata {error} ")
        else:
            print("islem basarıyla gerceklesti")
        finally:
            connect.close()
    @staticmethod
    def savemanystudents(liste):
        sql=("INSERT INTO `schooldb`.`student` (`studentnumber`, `name`, `surname`, `birhdate`, `gender`) VALUES (%s, %s,%s,%s,%s)")
        student.cursor.executemany(sql,liste)
        try:
            student.connect.commit()# aslında connectionu böylede kullanabiliriz aşağıda close oldugu yerde oldugu gibide
            print(f" {student.cursor.rowcount} tane satır eklenmistir ")
            print(f" son kaydın ıd si {student.cursor.lastrowid} ")
        except Exception as error :
            print(f"Hata {error} ")
        else:
            print("islem basarıyla gerceklesti")
        finally:
            connect.close()
# tarih=datetime.datetime.now().date()
# print(tarih)

# age=datetime.datetime(2003,8,25).date()
# print(age)
# days=(tarih-age)
# print(days.se)

referans=student("110","hasan","özcan",datetime.datetime(2004,6,2),"E")
deger=input("tek kayıtmı çok kayıtmı  1/many ")
if(deger =="1"):
    referans.saveonestudent()
else:
    student.savemanystudents(ogrenci)


