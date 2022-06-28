names=["Ali","Yağmur","Hakan","Deniz"]

years=[1998, 2000, 1998, 1987]
#1- "cenk" ismini listenin sonuna ekleyiniz
names.append("Cenk")
print(names)

#2- "Sena" değerini listenin başına ekleyiniz
names.insert(0,"Sena")
print(names)
#3- "Deniz" ismini listeden siliniz
names.remove("Deniz")
print(names)
#4- "Deniz" isminin indeksi nedir
names.insert(4,"Deniz")
print(names)
print(names.index("Deniz"))
#5- "Ali" listenin bir elemanı mıdır
bol="Ali" in names
print(bol)
#6- liste elemanlarını ters çevirin
names.reverse()
print(names)
names.reverse()
print(names)
#7- liste elemanlarını alfabetik olarak sıralayınız
names.sort()
print(names)
#8- years listesini rakamsal büyüklüğüne göre sıralayınız
years.sort()
print(years)
#9- str =" Chevrolet,Dacia" karakter dizisini listeye çeviriniz
str= "Chevrolet,Dacia"
str= str.split(",")
print(str)
#10- years dizisinin en büyük ve en küçük elemanı nedir
min= min(years)
max= max(years)
print(f"minimum değeri: {min} \nmaksimum değeri: {max} ")
#11- years dizisinde kaç tane 1998 değeri vardır
print(years.count(1998))
#12- years dizisinin tüm elemanlarını siliniz
years.clear()
print(years)
#13- kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız
sayi1= input("değerinizi giriniz: ")
sayi2= input("değerinizi giriniz: ")
sayi3= input("değerinizi giriniz: ")

str=sayi1+","+sayi2+","+sayi3
str=str.split(",")
print(str)


