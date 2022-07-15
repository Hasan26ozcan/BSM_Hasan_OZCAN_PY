import numpy as np
#1- (10,15,30,45,60) değerlerine sahip numpy dizisi oluşturunuz.
arr1=np.array((10,15,30,45,60))
print(arr1)


#2- (5-15) arasındaki sayılarla numpy dizisi oluşturunuz
arr2=np.arange(6,15)
print(arr2)

#3- (50-100) arasında 5'er 5'er artarak numpy dizisi oluşturunuz
arr3=np.arange(50,100,5)
print(arr3)

#4- 10 elemanlı sıfırdan oluşan bir dizi oluşturunuz
arr4=np.zeros(10)
print(arr4)

#5- 10 elemanlı birlerden oluşan bir dizi oluşturunuz
arr5=np.ones(10)
print(arr5)

#6- (0 100) arasında eşit aralıklarla 5 sayı üretin
arr6=np.linspace(0,100,5)
print(arr6)

#7- (10-30) arasında ratgele 5 tam sayı üretin
arr7=np.random.randint(10,30,5)
print(arr7)

#8- [-1 ile 1] arasında 10 adet sayı üretin
arr8=np.random.randn(10)
print(arr8)

#9- (3x5) boyutlarında (10-50) arasında ratgele bir matris oluşturunuz.
matriksil=np.random.randint(10,50,15)
matriks=matriksil.reshape(3,5)
print(matriks)

#10- üretilen matrisin satır ve sütun sayıları toplamlarını hesaplayınız
sutun= matriks.sum(axis=0)
satır= matriks.sum(axis=1) 
print(satır)
print(sutun)


#11- üretilen matrisin en büyük , en küçük ve ortalaması nedir

print(matriks.max())
print(matriks.min())
print(matriks.mean())

#12- üretilen matrisin en büyüğünün indeksi kaçtır
print(matriks.argmax())
print(matriks.argmin())
#13- (10- 20) arasındaki sayıları içeren dizinin ilk 3 elamnını seçiniz
arr10=np.arange(10,20)
print(arr10)
print(arr10[0:3])

#14- üretilen dizinin elemanlarını tersten yazdırın
print(arr10[::-1])

#15- üretilen matrisin ilk satırını seçiniz
print(matriks[0,:])

#16-üretilen matrisin 2. satır 3. sütündaki elemanı hangisidir
print(matriks[1][2])

#17- üretilen matrisin tüm satırdaki ilk elemanlarını seçiniz 
print(matriks[:,0])

#18- üretilen matrisin her bir elemanının karesini alınız
karesi= np.power(matriks,2)
karesi=matriks**2# üstekiyle aynı islevi yerine getiriyor
print(karesi)

#19- üretilen matris elemanlarnın hangisi pozitif çift sayıdır
#               aralığı (-50,+50) arasında yapınız
aralık= np.arange(-50,51)
print(aralık)
control1=aralık%2==0
çiftsayılar=aralık[control1]
print(çiftsayılar)
çiftvepozitif= çiftsayılar>0
sayılar=çiftsayılar[çiftvepozitif]
print(sayılar)







