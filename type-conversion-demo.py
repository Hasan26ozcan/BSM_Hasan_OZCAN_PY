"""
dairenin alanı: pi r^2
dairenin çevresi 2 pi r

yarıçapı verilen bir dairenin alanı ve çevresini hesaplayınız 
(pi : 3,14)


"""
from cmath import pi


a=7.4
a=int(a)
print(type(a))
print(a)





yarıcap =float(input("yarıçap değerinizi giriniz: "))
#inputtan her seferinde str deger geliyor bunu degistirmek istiyorsak gene onu ona atıyoruz
#eger en basta degerini girmek istiyorsak inputu o degerde girmesini istiyoruz

pi=3.14
print(yarıcap)
print(type(yarıcap))
#alt satirda yapilan islem yaricap float olursa bunu int cevirmemiz konusunda bize yardimci oluyor
#yarıcap=int(yarıcap)
#ama bu satira gerek yok
print(yarıcap)
print(type(yarıcap))
dairealanı=(pi)*(yarıcap**2)
dairecevresi=2*(pi)*yarıcap
print(dairealanı)
print(type(dairealanı))
#daire alan kısmı burada
print(dairecevresi)
print(type(dairecevresi))


print("Alan: ",dairealanı,"   Çevresi: ",dairecevresi) # int degerleri birlestirirken bosluk birakiyor 
# ama string degerleri birlestirirken bosluk birakmiyor
print("Alan: "+str(dairealanı)+"    Çevresi: "+str(dairecevresi))# burda hata vermesinin nedeni str degerleri sadece "+" degeri
#ile birlestirme olayı uygulanıyor




