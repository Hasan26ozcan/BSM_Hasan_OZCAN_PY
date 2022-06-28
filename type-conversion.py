# x=input("1. sayı: ")
# y=input("2. sayı: ")
# print(type(x))
# print(type(y))
# toplam=int(x)+int(y)
# print(type(x))
# print(type(y))
# print(toplam)


import re
from sqlite3 import connect


x =5            #int
y =2.9          #float
name="Çınar"    #str
isOnline=True   #boolean

# print(type(x))
# print(type(y))
# print(type(name))
# print(type(isOnline))

# x=float(x)
# print(x)
# print(type(x))

# y=int(y)
# print(y)
# print(type(y))

# result= str(x)+str(y)
# print(result)
# print(type(result))

# bool degeri string degere çevirelim

con=int(isOnline)
print(con)
print(type(con))

# burda gormemiz gereken en onemli sey true degeri int sayıya dondugunde 1 deger verir
#ama false degeri int sayıya dondugunde 0 degerini verir

canı=bool(199999)
# sadece 0 degerinde false degeri calisir diger butun degerlerde true degeri calısır
print(canı)

canım=float(True)
print(canım)
# bool bir degeri str cevirmek istedigimizde gene aynısını yazıyoruz
cansız=str(True)
print(cansız)






