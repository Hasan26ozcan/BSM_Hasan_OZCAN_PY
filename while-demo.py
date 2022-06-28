sayilar =[1,3,5,7,9,12,19,21]

#1: sayilar listesini while ile ekrana yazdırın
num =0
while( num< len(sayilar)):
    print(sayilar[num])
    num+=1
print("*"*100)
#2: başlangıç ve bitiş değerini kullanıcıdan alıp aradaki tüm
#   tek sayıları ekrana yazdırın
sayi1 =int(input("başlangıç değerinizi giriniz: "))
sayi2 =int(input("bitiş değerinizi giriniz: "))
indeks1= sayilar.index(sayi1) 
indeks2= sayilar.index(sayi2)
while (indeks1<indeks2-1):
    sayimiz=sayilar[indeks1+1]
    if(sayimiz%2 ==1):
        print(sayimiz)
    indeks1 +=1
print("*"*100)
sayi1= int(input("birinci sayiyi giriniz: "))
sayi2 =int(input("ikinci sayiyi giriniz: "))
while(sayi1<sayi2-1):
    sayimiz=sayi1+1 
    if(sayimiz%2 == 1):
        print(sayimiz)
    sayi1+=1




print("*"*100)
#3: 1-100 arasındaki sayıları azalan şekilde yazdırın
numbe = 99
while (numbe>0):
    print(numbe)
    numbe -=1

print("*"*100)

#4: kullanıcıdan alacağınız 5 sayıyı ekrana sıralı bir şekilde yazdırın.
counter=1
num=[]
while(counter <= 5):
    kul=int(input(f"{counter}. sayıyı giriniz:  "))
    num.append(kul)
    counter+=1
print(num)
num.sort()
coun=0
while(coun <len(num)):
    print(num[coun])
    coun +=1
#5: kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız
#   ** ürün sayısını kullanıcıya sorun
#   ** dictionary listesi yapısı (name,price) şeklinde olsun
#   ** ürün ekleme işlemi bittiğinde ürünleri ekrana while ile listeleyin
ürünsayısı =int(input("ürün sayınızı giriniz: "))
cou=0
dictionary={}
while(cou<ürünsayısı):
    isim =input("name bilginizi giriniz: ")
    fiyat =input("fiyat bilgisini giriniz: ")
    dictionary.update({
        cou :{
            "name": isim,
            "price": fiyat
        }
        
    
    }
    )
    cou+=1
print(dictionary)
sayaç=0
while(sayaç<cou):
    print(f"ürün adi {dictionary[sayaç]['name']} fiyat bilgisi : {dictionary[sayaç]['price']} ")
    sayaç+=1

urunler =[]
cou=0
dictionary={}
while(cou<ürünsayısı):
    isim =input("name bilginizi giriniz: ")
    fiyat =input("fiyat bilgisini giriniz: ")
    urunler.append({
            "name": isim,
            "price": fiyat
        }
    )
    cou+=1
sayaç=0
for urun in urunler:
    print(f" ürün adı: {urun['name']}  fiyat bilgisi {urun['price']} ")
#dışarda çift tırnak kuullandıysak içerde tek tırnak kullanmak zorundayız unutmayalım