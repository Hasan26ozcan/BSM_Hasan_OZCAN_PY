import pandas as pd
import numpy as np

data=pd.read_csv("nba.csv")
df=pd.DataFrame(data)
df.dropna(inplace=True,axis=0,how="all")
print(df)
#1- ilk 10 kaydı getiriniz?
print(df.head(10))
#2- toplam kaç kayıt vardır?
print(df.info)
print(df.size)
print(df.columns)
print(df.shape)
print(len(df.index))
#3- tüm oyuncuların toplam maaş ortalamsı nedir
result=df["Salary"].dropna(axis=0,how="any")
maasıolanoyuncular=result.mean()
print(maasıolanoyuncular)
#4- en yüksek maaş ne kadardır?


# df=df.sort_values("Salary",ascending=False)
# maxsalary=df["Salary"]
# print(maxsalary[103])


print(df["Salary"].max())
#5- en yüksek maaşı alan oyuncu kimdir
# bu benim yaptığım 
maksmaas=df["Salary"].max()
mas=df.groupby("Salary").get_group(maksmaas)
print(mas["Name"].iloc[0])

# bu da hocanın yaptığı
result=df[df["Salary"]==df["Salary"].max()]["Name"].iloc[0]
print(result)



#6- yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takım
df[["FirstName","Lastname"]]=df["Name"].loc[df["Name"].str.split().str.len()==2].str.split(expand=True)
print(df)

control=(df["Age"]>=20) & (df["Age"]<25)
yas2025=df[control]
yas2025["ikisini_bir_arada"]=df["FirstName"]+"   "+df["Team"]

print(yas2025["ikisini_bir_arada"])

print(yas2025[["FirstName","Team","Age"]].sort_values("Age",ascending=False))





#***********************************************************************************************
# control1=df["Age"]
# trsa=(control1>20) & (control1<25)
# print(control1[trsa])# bunu asla unutma control1 ve df ile yapman arasındaki farkı sakın unutma 
#*************************************************************************************************





#7- "John Holland" isimli oyuncunun oynadığı takım hangisidir

asd=df.groupby("Name").get_group("John Holland")
print(asd)
print(asd["Team"].iloc[0])


#8- Takımlara göre oyuncuların ortalama maaş bilgisi nedir



sat=df.groupby("Team")["Salary"].mean()
print(sat)

#9- kaç farklı takım mevcut ?

teambilgi=df["Team"].unique()
print(len(teambilgi))


#10- her takımda kaç oyuncu oynamaktadır



say=df.groupby("Team")["Name"].count()
print(say.sort_values(ascending=False))

#11- ismi içinde "and" geçen kayıtları bulunuz

# def sayas(str,sasd="and"):
#     if(str in  sasd):
#         return True
#     else:
#         return False


andname=df["Name"].str.lower().str.contains("and")
print(df[ andname])


def str_find(name):
    if "and" in name.lower():
        return True
    else:
        return False

result=df["Name"].apply(str_find)
print(df[result])


