import pandas as pd
import numpy as np


data=np.random.randint(10,100,15).reshape(5,3)
df=pd.DataFrame(data,index=["a","c","e","f","h"],columns=["column1","column2","column3",])
print(df)
df=df.reindex(["a","b","c","d","e","f","g","h"])
print(df)

resul=df

sa=resul.drop("g",axis=0)
print(sa)
sa=resul.drop(["column1","column2"],axis=1)
print(sa)
sa=resul.drop(["b","d","g"],axis=0)
print(sa)

nullplace=df.isnull()
print(nullplace)
notnullplace=df.notnull()
print(notnullplace)

# kolonlardaki nan olan yerlerin sayısı öğrnemke için 


columncounter=df.isnull()
print(columncounter)


columncount=df.isnull().sum()

print(columncount)

kol2null=df["column2"].isnull().sum()
print(kol2null)


newcolumn=[np.nan,30,np.nan,51,np.nan,40,np.nan,78]
df["column4"]=newcolumn
print(df)
column=df.loc["g"].isnull().sum()
print(column)

columns=df["column2"].isnull()
result=df[columns]["column2"]
print(result)

columns=df["column2"].notnull()
result=df[columns]["column2"]
print(result)



results=df.dropna(axis=0)
# axis=> 0 yani satıra göre silme işlemi yapar eger o satırda 1 tane bile nan degeri varsa o satırı almamamızı saglar
results=df.dropna(axis=1)
# ama eger boyle yaparsak axis=1 yaparsak o zamanda sutüna göre islem yapmamız gerekiyor
print(results)

results=df.dropna(how="all")# böyle yaparsak eger sadece bütün hepsi nan olan satırları bize getirmez ("g") yok 
print(results)


results=df.dropna(how="any")# burda ise normal bizim bildigimiz sekilde yapılan islem
print(results)
# eger sadece bir yerde kullanmak istersek eger söyle yapıyoruz

results=df.dropna(subset=["column1","column2"],how="all")
results=results.loc[:,["column1","column2"]]
print(results)



results=df.dropna(subset=["column1","column2"],how="any")
# herhangi bir tanesinde nan varsa o zaman orda onu ekrana yazdırtmayız
print(results)

results=df.dropna(thresh=4)# 4 tane degeri olanları bize getiriyor gerisini getirmiyor
# yani en az sayıda normal veri
print(results)


# df=df.fillna(value=1)
print(df)

# şimdi sadece sayı olanların sayıları toplamlarını bulalım


def ortalama(df):
    dolu=df.sum().sum()
    uzunluk=df.size
    nan=df.isnull().sum().sum()
    doluluk=uzunluk-nan
    return dolu/doluluk


print(ortalama(df))

df=df.fillna(value=ortalama(df))

print(df)