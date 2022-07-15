import pandas as pd

apple=[10,2,3,4,5]
orange=[0,5,1,2,6]
series1= pd.Series(apple)
series2= pd.Series(orange)

datamız=dict(apple=series1,orange=series2)

dtframe=pd.DataFrame(datamız)
print(dtframe)



df=pd.DataFrame([12,3,2123,5,73])
print(df)

data=[["ahmet",50,67],["mehmet",20],["samet",10],["atilla",100]]
df=pd.DataFrame(data=data)
print(df)


df=pd.DataFrame(data=data,columns=["money","salary","sold"],index=["a","b","c","d"],dtype=float)# kaç tane varsa o kadar column eklemeliyiz yani kolon grubunun
# baştan sona dzenlenmesini kendimiz yapabiliriz ve indeks ilgilerini de kendimize göre değiştirebiliriz
print(df)

df =pd.DataFrame()
print(df)
# burda da anlaşıldıgı gibi column ve index yerleri boş oalrak duruyor yanni buraları kendimize göre degistirebilriz

# eger burdaki volumn ya da index bilgisi yazmadan yapmak istersek eger yapmamız gerek sıra
#       data,index,column olarka söyleyebiliriz



# ama bütün bu işlemleri daha rahat yapmak istersek dictionary işlemiyle daha rahat yapabiliriz 

dict={"Name": ["ahmet","mehmet","samet","atilla"],"Grade":[50,20,10,100],"salary":[60,None,None,None] }

sınır=pd.DataFrame(dict,index=[1,2,3,4])
print(sınır)

#çok daha iyisi ise

dic_list=[
        {"name":"ahmet","grade":50},
        {"Name":"mehmet","grade":20},
        {"name":"samet","grade":10},
        {"name":"atilla","grade":100}
        ]
 
listesi= pd.DataFrame(dic_list)
print(listesi)









