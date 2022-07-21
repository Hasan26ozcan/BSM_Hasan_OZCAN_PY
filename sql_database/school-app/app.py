import imp
from dbmanager import dbmanager
import datetime
from student import student
class app:
    def __init__(self):
        self.db=dbmanager()
    def initapp(self):
        msg="****\n1-ogrenci listesini getir\n2-ogrenci ekle\n3-ogrenci güncelle\n4-ogrenci sil\n5-ogretmen ekle\n6-sınıflara göre dersler\n7- çıkış(E/Ç)\n8-****"
        while True:
            print(msg)
            a=input("seçim: ")
            a=a.upper()
            if (a=="1"):
                self.studentdisplay()
            elif(a=="2"):
                self.addstudent()
            elif(a=="3"):
                self.editstudent()
            elif(a=="4"):
                self.deletestudent()
            elif (a=="E") or (a=="Ç") :
                break
            else:
                print("yanlış seçim yaptınız")

    def deletestudent(self):
        self.displaystudents()
        stdn1=input("student id")
        self.db.deletestudent(stdn1)


    def editstudent(self):
        self.displaystudents()
        studentid=int(input("student id"))
        students=self.db.getstudentbyıd(studentid)
        students[0].name=input("name: ")or students[0].name
        students[0].surname=input("surname: ")or students[0].surname
        students[0].gender=input("gender(E/K): ")or students[0].gender
        students[0].classıd=int(input("sınıf: "))or students[0].classıd

        year=int(input("year: ")) or students[0].birhdate.year
        mounth=int(input("mounth: ")) or students[0].birhdate.month
        day=int(input("day: ")) or students[0].birhdate.day

        students[0].birhdate=datetime.date(year,mounth,day)

        self.db.editstudent(students[0])




    def displaystudents(self):
        self.displaysclasses()
        classid=input("hangi sınıf: ")
        students=self.db.getstudentbyclassıd(classid)
        print("öğrenci listesi")
        for std in students:
            print(f"{std.id} {std.name} {std.surname}  ")
        
        return classid
    def addstudent(self):
        self.displaysclasses()
        classıd=int(input("classıd: "))
        number=(input("numara: "))
        name=(input("ad: "))
        surname=(input("soyad: "))
        year=int(input("yıl: "))
        mounth=int(input("ay: "))
        day=int(input("gün: "))
        birthdate=datetime.date(year,mounth,day)
        gender=input("cinsiyet(E/K): ")
        
#    def __init__(self,id,studentnumber,name,surname,birhdate,gender,classid):
        studentS=student(None,number,name,surname,birthdate,gender,classıd)
        self.db.addstudent(studentS)
    def displaysclasses(self):
        classes=self.db.getclassed()
        for i in classes:
            print(f"{i.id}, {i.name} ")


    def studentdisplay(self):
        self.displaysclasses()
        classes=self.db.getclassed()
        for i in classes:
            print(f"{i.id}, {i.name} ")
        classid=input("hangi class id: ")
        students=self.db.getstudentbyclassıd(classıd=int(classid))
        for index,i in enumerate(students):
            print(f" {index}. => {i.id},{i.name} {i.surname} ")






apps=app()
apps.initapp()
list=apps.studentdisplay()
    



