from telnetlib import PRAGMA_HEARTBEAT
import pandas as pd
from numpy.random import randn

df =pd.DataFrame(randn(3,3),index=["A","B","C"],columns=["column1","column2","column3"])

print(df)
result=df["column1"]
print(type(result))


result=df[["column1","column2"]]
print(result)
# loc=[row,column]
# sadece bir satır seçmek istiyorsak o zaman loc["row"]
# sadece bir column seçmek istiyorsak o zaman loc[":","column"] yaparak yapabilriz

result=df.loc["A"]# loc ile o satırdaki degerleri ekrana yazdırmasını saglıyoruz
print("**"*50)
print(type(result))
print(result)

result=df.loc[:,"column1"]
print(result)


result=df.loc[:,["column1","column2"]]
print(result)

result=df.loc[ :,"column1":"column3"]
# bu aralıktakilerin hepsini ekrana yazdırmamızı sağlara am unutmayalım son degerde içine girer
print(result)

result=df.loc[ :,:"column2"]
print(type(result))
print(result)

result=df.loc[:"B",:"column2"]
print(type(result))
print(result)
# ama biz burda yine indeks ile çalışmak istiyorsak eger
result=df.iloc[2]# iloc kullanarak normal verdiğimiz indeksleri bizim bildigimiz sayılara göre indirgiyor
print(result)
result=df.loc["C"]# yani bu ikisi aynı islemi yapıyor
print(result)
# eger tek bir deger almak istersek eger

result=df.loc["A","column1"]
print(result)

result=df.loc[["A","B"],["column1","column2"]]
print(result)

df["column4"]=pd.Series(randn(3),index=["A","B","C"])
print(df)

df["colum5"]=df["column1"]+df["column4"]
print(df)


df.drop("colum5",axis=1)
print(df)


# ama eger buradaki degeri hiçbir yere atmadan kullanıyorsak eger inplace ile True yaparsak orda kalıcı olarak yapmış oluruz

df.drop("colum5",axis=1,inplace=True)
print(df)


stack=[1,2,3,5,6]
sayi= stack.pop()
print(sayi)
