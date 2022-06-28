"""

    1-100 arasında rastgele üreticilerek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın
    ** "random" modülü için "pyton random " şeklinde arama yapın
    ** 100 üzerinden puanlama yapın. Her soru 20 puan
    ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplayınız

"""
import random
randoms = random.randint(1,100)
print(randoms)
haksayısı =int(input("kaç denemeden bulucağınızı düşünüyorsunuz: "))
counter=0
countrandom=0
liste=[]
doogrusırası=0
while(counter<haksayısı):
    print(randoms)
    print(f" {countrandom+1}. sorunuz için")
    sayiniz =int(input("sayınızı giriniz:  "))
    if(sayiniz<randoms):
        print("sayinizi büyük giriniz: ")    
    elif(sayiniz>randoms):
        print("sayinizi küçültünüz:")
    else:
        print("sayınız doğru sonucu ulaşmıştır ")
        doogrusırası=counter
    counter+=1
    if((counter>=haksayısı or sayiniz==randoms)  and  countrandom< 5 ):
        randoms = random.randint(1,100)
        print(haksayısı)
        can=(100-((100/haksayısı) *(counter-1)))
        liste.append((countrandom,can))
########can=(100-((100/haksayısı) *(doogrusırası))
        countrandom+=1
        counter=0
        doogrusırası=0
    if(countrandom == 5):
        break
print("100 olanla ")
print(liste)
print("eğer hiç birşey doğru yapamazsada genede puan")
#hiç bulamadık o zaman 0
# sonda bulduk o zaman 100
#başta bulduk o zaman en az yüzdelik dilimi hangisi oluyorsa o
print("***"*50)
print("üsteki yaptığım benşm kendi kişisel yaptığım hocanınkisi aşağıda".rjust(100))

import random

sayi =random.randint(1,100)
haksayisi =int(input("kaç hakkınızı olsun:  "))
counter=0
print(sayi)
while(haksayisi>counter):
    tahmin =int(input(f" {counter+1}. tahminizi giriniz: "))
    if(tahmin>sayi):
        print("tahmininizi küçültünüz: ")
    elif(tahmin<sayi):
        print("tahmininizi büyültünüz: ")
    else:
        print(f"tebrikler {counter+1}. tahimde bildiniz puanınız ise {100-((100/haksayisi) *(counter))}  ")
        break
    counter+=1
    if(counter == haksayisi):
        print(f"bilemediniz tahmin sayımız: {sayi} ve puanınız 0 ")
        break
























