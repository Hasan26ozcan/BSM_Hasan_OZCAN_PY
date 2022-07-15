import random
import numpy as np



result=np.array([1,2,3,4,5,6,7,8,9])
print(result)

for i in result:
    print(i)

results=np.array(range(1,10))
print(results)
resultsa=np.arange(1,10)
print(resultsa)

resultsan=np.arange(10,101,3) #normal range metoduyla aynı islevi yapiyor
print(resultsan)

results=np.zeros((10))# bize kaç tane 0 olması gerektiğiniz söylüyor
print(results)


results=np.ones(10) # budurmda ise bize o kadar sayıda 1 rakamını getiriyor
print(results)

results=np.linspace(0,100,20)# verdiğimiz aralığı eşit aralıklarla o sayı kadar böler
print(results)

results=np.linspace(0,10,5)
print(results)


results=np.random.randint(6,100)
print(results)


results=np.random.randint(0,100,20)# 0 ve 100 arasındaki random 20 sayıyı diziye eklememizi saglıyor
print(results)

results=np.random.rand(5)# 0 ve 1 arasındaki random 5 sayıyı listeye ekliyor
print(results)


results=np.random.randn(5)# 0 ve 1 arasında 5 sayıyı bize getirir ama işin içine bu seferde negatiflerde girer
print(results)

np_arrays=np.arange(0,50)
print(np_arrays)
np_multi=np_arrays.reshape(5,10)
print(np_multi)
print(np_multi.sum(axis=1))# satır satır toplamamızı saglıyor
print(np_multi.sum(axis=0))# sütun sütun toplamamızı sağlıyor


print(np_multi.shape)
print(np_arrays.shape)

rnd_numbers=np.random.randint(0,100,10)
maks_sayı=rnd_numbers.max()
min_sayı=rnd_numbers.min()
orta_sayı=rnd_numbers.mean()# üretilen sayıların bir ortalamasını bize verir
print(rnd_numbers)
print(maks_sayı)
print(min_sayı)
print(orta_sayı)

inkdesimaksimumun=rnd_numbers.argmax()
print(inkdesimaksimumun)

inkdesiminimumun=rnd_numbers.argmin()
print(inkdesiminimumun)


