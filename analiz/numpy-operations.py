from cmath import sin
import numpy as np


numbers1=np.array(np.random.randint(10,100,6))
print(numbers1)
numbers2=np.array(np.random.randint(10,100,6))
print(numbers2)


result=numbers1+numbers2 # iki dizininde aynı indeksteki sayılarını toplayıp bir dizi oluşuturulmasını sağlıyoruz
print(result)

result=numbers1 +10
print(result)


result=numbers1-numbers2
print(result)

result=numbers1-10
print(result)

result=numbers1*numbers2
print(result)

result=numbers1*10
print(result)

result=numbers1/numbers2
print(result)

result=numbers1/10
print(result)

result=np.sin(numbers1)
print(result)

result=np.cos(numbers1)
print(result)

result=np.sqrt(numbers1)
print(result)

result=np.log(numbers1)
print(result)

multi_numbers1=numbers1.reshape(2,3)
multi_numbers2=numbers2.reshape(2,3)

print(multi_numbers1)
print(multi_numbers2)

result=np.vstack((multi_numbers1,multi_numbers2))
print(result)
# v stack verilen dizilerin yatay olarak birşeltirilmesini saglar
sayi=result.ndim
print(sayi)
result=np.hstack((multi_numbers1,multi_numbers2))
print(result)

result= numbers1 >=50# aslıdna burda for döngüsü açıpta yaptığımız islemi daha pratiğe indirmis halde karsımıza cıkıyor
# butun elemanların 50 ten büyük olup olmadıgına bakmamızı saglıyor
print(result)
print(numbers1)

result=numbers1%2==0# sayının tek çiftliğine göre kontrol yapıyoruz
print(result)

print(numbers1[result]) # sadece True degerleri olanları ekrana yazdırıyor
#sadece true olan degerleri bize getiriyor
print(result)

