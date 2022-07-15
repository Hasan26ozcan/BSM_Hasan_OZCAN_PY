import pandas as pd

df= pd.read_csv("credits.csv")
print(df)
# bu sayede csv dosyasını rahat bir şekilde okuyabiliyoruz


df=pd.read_json("sample.json",encoding="UTF-8")
print(df)


df=pd.read_excel("veriEkselTabloOrnek.xls")
print(df)