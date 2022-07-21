
from datetime import datetime
from connection import connect


class student:
    connect=connect
    curor=connect.cursor()
    def __init__(self,id,studentnumber,name,surname,birhdate,gender):
        if(id==None):
            self.id=0
        else:
            self.id=id
        self.studentnumber=studentnumber
        self.name=name
        self.surname=surname
        self.birhdate=birhdate
        self.gender=gender
    @staticmethod
    def idogrenciupdate(id):
        sql="SELECT * FROM schooldb.student where id=%s"
        values=(id,)
        student.curor.execute(sql,values) 
        try: 
            return student.curor.fetchone()
        except Exception as err:
            print(f"hata {err} ")
    def update(self):
        sql="UPDATE schooldb.student SET studentnumber=%s,name =%s,surname=%s,birhdate=%s,gender=%s WHERE id =%s"
        values=(self.studentnumber,self.name,self.surname,self.birhdate,self.gender,self.id)
        student.curor.execute(sql,values)
        try: 
            student.connect.commit()
        except Exception as err:
            print(f"hata {err} ")

    @staticmethod
    def genderupdate(gender):
        sql="select * from schooldb.student where gender=%s"
        values=(gender,)
        student.curor.execute(sql,values)
        try: 
            return student.curor.fetchall()
        except Exception as err:
            print(f"hata {err} ")
    def listupdate(list):
        sql="UPDATE schooldb.student SET studentnumber=%s,name =%s,surname=%s,birhdate=%s,gender=%s WHERE id =%s"
        value=[]# gelen liste bizim istedigimiz sırada degil o yüzden onu istedigimiz sıraya sokamamız gerekiyor
        order=[1,2,3,4,5,0]
        for item in list:
            values=[]
            for i in order:
                values.append(item[i])
            value.append(values)
        print(value)

        student.curor.executemany(sql,value)



        try: 
            student.connect.commit()
        except Exception as err:
            print(f"hata {err} ")



# 5- aşağıdaki güncelleme sorularını yapınız
#   a-id'e göre aldıgınız bir ogrencinin bilgilerini güncelleyiniz
#student.idogrenciupdate(11,112,"fatma","kesik",datetime.datetime(2004,2,4),"K")
#   b- cinsiyet e göre aldıgınız bir ogrencinin bilgilerini güncelleyiniz
mysq=student.idogrenciupdate(6)
print(mysq[0])
my=student(mysq[0],mysq[1],mysq[2],mysq[3],mysq[4],mysq[5])
my.name="kemalcan"
my.surname="kemalcan"
my.update()


myyqli=student.genderupdate("E")
print(myyqli)
liste=[]
for i in myyqli:
    i=list(i)
    i[2]="MR "+i[2]
    liste.append(i)

student.listupdate(list=liste)













