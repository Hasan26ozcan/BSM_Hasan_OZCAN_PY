from unicodedata import name


sayilar=[1,3,5,7,9,12,19,21]

#1- sayılar listesindeki hangi sayılar 3'ün katıdır
for sayi in sayilar:
    if(sayi%3 ==0):
        print(sayi)
print(sayilar)
#2- sayilar listesindeki sayıların toplamı kaçtır
toplam =0
for sayi1 in sayilar:
    toplam +=sayi1
print(toplam)
print(sayilar)
#3- sayilar listesindeki tek sayıların karesini alınız
for sayi2 in sayilar:
    if (sayi2%2==1):
        print(sayi2**2)
print(sayilar)

sehirler=["kocaeli","istanbul","ankara","izmir","rize"]
#4- şehirlerden hangileri en fazla 5 karakterlidir
for sehir in sehirler:
    if(len(sehir)<=5):
        print(sehir)

urunler=[
    {"name":"samsung s6", "price": "3000" },
    {"name":"samsung s7", "price": "4000" },
    {"name":"samsung s8", "price": "5000" },
    {"name":"samsung s9", "price": "6000" },
    {"name":"samsung s10", "price": "7000" }
]
#5- ürünlerin fiyatları toplamı nedir
top=0
for urun in urunler:
    print("*"*100)
    for ur in urun:
        print(urun[ur])
    top+=int(urun["price"])
print(urunler)
print(top)
#6- ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz
for urun in urunler:
    if(int(urun["price"])<=5000):
        print(urun["name"])
print(urunler)