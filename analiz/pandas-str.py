from cgitb import reset
from tokenize import Name
import pandas as pd

read=pd.read_csv("nba.csv")
print(read)
df=pd.DataFrame(read)
print(df)



df.dropna(inplace=True,axis=0)# satır için
print(df)
print(df.columns)

df.dropna(axis=0,inplace=True)
print(df)


df["Name"]=df["Name"].str.upper()
print(df.head(10))


df["index"]=df["Name"].str.find("a".upper())
print(df)

result= df["Name"].str.contains("jordan".upper())
print(df[result])

result=df["Team"].str.replace(" ","-").str.replace("Ce","ce")
print(result.head(5))
print(result.tail(5))
df[["firstname","lastname"]]=df["Name"].loc[df["Name"].str.split().str.len()==2].str.split(expand=True)
print(df.head(10))

# bu benim yaptıgım bu biraz daha farklı # ama anlaşılması güzel bir algoritma
df[["firtname","Lastname"]]=df.loc[:,"Name"].loc[df.loc[:,"Name"].str.split().str.len()==2].str.split(expand=True)
print(df)



sayım=df["Name"].str.split().str.len()==2
print(df[sayım])
results=df[sayım]


df[["ilk ad","soyad"]] = results["Name"].str.split(expand=True)
print(df)




