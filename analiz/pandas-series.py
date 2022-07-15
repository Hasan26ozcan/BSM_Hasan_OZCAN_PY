# yapılan herşey aynı trüde olmak zorunda değil

import pandas as pd
import numpy as np

numbers=[10,20,30,40,50]
letters=["a","b","c","d","e"]
complex=["a",2,True,4.2]
scalar=5


# pandas_series=pd.Series()
pandas_series=pd.Series(numbers)
#pandasta otomatikmen sıraya göre indeks numarasaı atama işlemi yapıyor
print(pandas_series)

pandas_series=pd.Series(letters)
print(pandas_series)

pandas_series=pd.Series(complex)
print(pandas_series)

# normal bir değer girsek bile unu listeye çevirip öyle kullanıyor
pandas_series=pd.Series(scalar)
print(pandas_series)

pandas_series=pd.Series(scalar,[0,1,2,3])
# tek sayımız var ama onund asayısından fazla indeks var o zaman onun sayısı kadar arttırılma islemi yapar
# ya indeks sayısı kadar deger girilecek ya da 1 tane deger girilecek aksini zaten kabul etmiyor
print(pandas_series)

pandas_series=pd.Series(numbers,["a","b","c","d","e"])
# istersekte kendi indeksimizi verebiliriz
print(pandas_series)

dic={"e":10,"d":20,"c":30,"b":40,"a":50}

pandas_series=pd.Series(dic,)# ama eger bir sözlük yapısı varsa hem key hem value degeri oldugu için key degeri indekse yazılıyor
print(pandas_series)
# ama eger indekslerini degistirrmek istersek gene sag tarafa yazarız ve onlar onun indeks bilgisi yerine gecer

random_numbers=np.random.randint(10,100,6)
pandas_series=pd.Series(random_numbers)
print(pandas_series)
pandas_series=pd.Series(numbers,["a","b","c","d","e"])
# amaa bir farkı olarak indek numara ile sayı arasında bir fark
# sayı ile yaptığımızda o sayıyı almayız çünkü indeksler 0 dan başlıyor ama 
# harf ile yaptığımızda ordaki segeride ekrana yazdırmasını saglıyor
print(pandas_series[0])
print(pandas_series[-1])
print(pandas_series[:2])
print(pandas_series[-2:])
print(pandas_series["a"])
print(pandas_series["d"])
print(pandas_series[:"c"])
result=pandas_series[["a","d","e"]]
print(result)
print(pandas_series.ndim)
print(pandas_series.dtype)
print(pandas_series.shape)
print(pandas_series.sum(axis=0))#======= print(pandas_series.sum()) aynı şeylerdir
print(pandas_series.max())
print(pandas_series.min())
print(pandas_series.mean())
result=pandas_series*2
print(result)
result=np.sqrt(pandas_series)
print(result) 
boll= pandas_series>=30
boll=pandas_series %2==0
print(boll)
print(pandas_series[boll])


opel2018=pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
opel2019=pd.Series([40,30,20,10],["astra","corsa","Grandland","insignia"])

opels=opel2018+opel2019
print(opels)
print(opels["astra"])
#print(opels["combo"])