#1-"Bmw, Mercedes,Opel,Mazda" elemanlarına sahip bir liste oluşturunuz
list1=["Bmw","Mercedes","Opel","Mazda"]
print(list1)
#2- listede kaç eleman vardır
print(len(list1))
#3-listenin ilk ve son elemanı nedir
print(f"listenin ilk elemanı: {list1[0]} \nlistenin son elemanı {list1[len(list1)-1]} ")

#4-Mazda değerini Toyata ile değiştirin
indeksi=list1.index("Mazda")
list1.insert(indeksi,"Toyata")
list1.remove("Mazda")
print(list1)
# yukarda metotları kullanarak yaptım ben aşağıda daha basit halde yapılmış hali var
list1[-1]="Toyata"

#5-Mercedes listenin bir elemanımıdır
result="Mercedes" in list1
indeks=list1.index("Mercedes")
print(indeks)
print(result)
#6-Listenin -2 indeksindeki değer nedir
print(list1[-2])
#7-listenin ilk 3 elemanını alın
list2=list1[0:3]
print(list2)
#8- Listenin son 2 elemanı yerine "Toyata" ve "Renault" değerlerini ekleyin
sayi1= list1[len(list1)-1]
sayi2= list1[len(list1)-2]
list1.remove(sayi1)
list1.remove(sayi2)
list1.append("Toyata")
list1.append("Renault")
print(list1)
#9-Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin
list1.append("Audi")
list1.append("Nissan")
print(list1)
#10-listenin son elemanını silin

#silme işlemi için 

del list1[-1]
print(list1)
list1.remove(list1[len(list1)-1])
print(list1)
#11-listedeki elemanları tersten yazdırın
# list1.reverse()
# print(list1)
# list1.reverse()
list1=list1[::-1]
print(list1)

#12-Aşağıdaki verileri bir liste içinde saklayınız
        #studenta: yiğit bilgi 2010, (70,60,70)
        #studentb: sena turan  1999, (80,80,80)
        #studentc: Ahmet Turan 1998, (80,70,90)
studenta= ["yiğit"," bilgi", 2010, [70,60,70]]
studentb= ["sena turan" , 1999, [80,80,80]]
studentc= ["Ahmet Turan", 1998, [80,70,90]]
list3=[studenta,studentb,studentc]
print(f" {studenta[0]} {studenta[1]}  {2019-studenta[2]} yaşında ve not ortalaması {((studenta[3][0]+studenta[3][1]+studenta[3][2])/3) :1.3} ")
# #13- liste elemanlarını ekrana yazdırın
print(list3[0][3][1])












