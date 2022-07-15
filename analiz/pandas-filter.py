import pandas as pd
import numpy as np
nuyp=np.random.randint(10,100,75)
array=nuyp.reshape(15,5)

df= pd.DataFrame(array,columns=["column1","column2","column3","column4","column5"])
print(df)

print(df.loc[:,"column1"])
print(df.columns)# bizim column bilgilerimizi buraya getirmesini saglıyor
print(df.head())
print(df.head(7))# en başındakilerden itibaren getirir
print(df.tail())# en sonundakileriden itibaren getirir

# mesela kayıtlardan sadece column1 in sadece ilk 5 kayıdı istersek eger
print(df.loc[:,"column1"].head()) #burda oldugu gibi şunu da yapabiliriz #df.column1.head()
print(df.loc[:,["column1","column2"]].head())
print(df.loc[5:15,:"column2"].head())

result= df>50
print(result)
print(df[result])


result= df%2==0
print(result)
print(df[result])

result= df.loc[:,:"column2"]%2==0
print(result)
print(df.loc[:,:"column2"][result])
# print(df[result][:,:"column2"])


result=(df.loc[:,"column1"]>50) & (df.loc[:,"column1"]<70)# ikiside doğru
print(df[result][["column1","column2"]])
result=(df.loc[:,"column1"]>50) & (df.loc[:,"column2"]<70)# ikiside dogru
print(df[result][["column1","column2"]])
result=(df.loc[:,"column1"]>50) | (df.loc[:,"column2"]<70)# sadece 1 tanesi dogru olması yeter
print(df[result].loc[:,["column1","column2"]])
print(df)
# query içine koşullarımızı girebiliyoruz meselea söyle
result=df.query("column1>=50 & column1 % 2 == 0")
print(result.loc[:,:"column2"])




result=df.query("column1>=50 | column1 % 2 == 0")
print(result.loc[:,:"column2"])









