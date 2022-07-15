from optparse import Values
import pandas as pd
import numpy as np

data={
    "Column1":[1,2,3,4,5,6],
    "column2":[10,20,13,45,25,13],
    "column3":["abc","bca","adeeeeee","cba","dea","abc"]
}

def kareal(x):
    return x**2
# burda ise tama olarak kare alma şlemini yapıyoruz


kareal2=lambda x:x**2
df=pd.DataFrame(data=data)
result=df["column2"].unique()# uniqe sayesinde burada tekrara izin vermeden yapmasını saglıyor
print(result)
result=df["column2"].nunique()# başındaki n sayesinde kaç tane oldugunu öğrenmiş oluyoruz
print(result)
result=df["column2"].value_counts()# bir degerden kaç tane oldugunu ogrenmemizi saglıyor
print(result)
result=df["column2"].apply(kareal)
print(result)
# kare alma işlemini yaptıgımızda normal her zamanki gibide yapabiliriz ama eger bir donksiyonu kullanmak istiyorsak
# o zaman apply metodu içinde fonksiyonu çağırarak o satırdaki her degeri o metodu kullanarak ordaki işlemi yaparak tekrardan 
# satıra eklemesini saglıyor

result=df["column2"].apply(kareal2)
print(result)

df["column4"]=df.loc[:,"column3"].apply(len)

result=df.loc[:,"column3"].str.len()
print(result)
print(df)

print(df.columns)
print(df.index) # 0 dan başlayarak 6 ya kadar 1 er 1 er artarak ilerliyor
print(len(df.columns))
print(len(df.index))

sıralanması=df["column2"].sort_values()
df["column2"]=sıralanması
print(df)
print(df.index)

df=df.reindex([0,1,2,3,4,5,6])
print(df)
df=df.drop(6,axis=0)
print(df)
df=df.sort_values("column2")
print(df)

# df["column4"]=df["column4"].sort_values()
# print(df) 
# ama bu islem çalışmıyor eger sadece bu lazımsa işey yarar ama normal kullanmak istersek işey yaramaz

df=df.sort_values("column3")
print(df)



# sort sıralamasında az dan çoga dogru oluyor ama biz çoktan aza doğru olmasını isterske o zaman ascending kullanmamız gerekir şöyle

df=df.sort_values("column2",ascending=False)
print(df)

data={
    "Ay":["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori":["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir":[20,30,15,14,32,42,12,36,52]
}

df=pd.DataFrame(data=data)
print(df)
print(df["Ay"].unique())
print(df["Kategori"].unique())
print(df["Gelir"].unique())
df=df.sort_values("Gelir",ascending=False)
print(df)

print(df.pivot_table(index="Ay",columns="Kategori",values="Gelir"))
print(df)

