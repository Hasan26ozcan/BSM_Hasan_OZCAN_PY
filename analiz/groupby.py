import pandas as pd
import numpy as np

personeller={
    "Çalışan":["Ahmet Yılmaz","Can Ertürk","Hasan Korkmaz","Cenk Saymaz","Ali Turan","Rıza Ertürk","Mustafa Can"],
    "Departman":["insan kaynakları","bilgi işlem","muhasebe","insan kaynakları","bilgi işlem","muhasebe","insan kaynakları"],
    "yaş":[30,25,45,50,23,34,42],
    "semt":["kadıköy","tuzla","maltepe","tuzla","kadıköy","tuzla","maltepe"],
    "maas":[5000,3000,4000,3500,2750,6500,4500]
}
df=pd.DataFrame(personeller)
print(df)
toplammaas=df.loc[:,"maas"].sum()
print(toplammaas)
ortalamamaas=df.loc[:,"maas"].mean()
print(ortalamamaas)

result=df.groupby("Departman").groups
print(result)


# ama eger burada iki den fazla column da yapmak istersek işimizide daha da rahat kolay yaparız 

result=df.groupby(["Departman","semt"]).groups
print(result)
print("**"*50)
semtler=df.groupby("semt")
print(semtler.groups)
for name,group in semtler:# burda name bizim semtlerdeki isimlerimiz kolun isimlerimiz
    print(name)           # ama group dediğimiz şey ise o semtin diger özelliklerinin hepsi olarak söyleyebiliriz
    print(group)

departman=df.groupby("Departman")
print("**"*50)
for name,group in departman:
    print(name)
    print(group)
print("//"*50)
# burada ise bizim seçtiğimiz kolndan istediğimiz gruba uyanları sınırlandırmasını sağlamış oluyoruz
semtimiz=df.groupby("semt").get_group("tuzla")
print(semtimiz)
masorta=semtimiz.loc[:,"maas"].mean()
print(masorta)

# ama eger sadece bizim seçtiğimiz column kolon yerindeki bütün hepisini hesaplasın

dep=df.groupby("Departman").mean()
print(dep)

# semtlere göre oturanların yas ortalamaları
yas=df.groupby("semt")["yaş"].mean()
print(yas)

# semtlere göre maaş ortalamaları için ise söyle
yas=df.groupby("semt")["maas"].mean()
print(yas)

#semtlere göreçalışna kişi sayısı alalım

sayısı=df.groupby("semt")["Çalışan"].count()
print(sayısı)

# en fazla yaşı olanı bulalım
agemax=df.groupby("Departman")["yaş"].max()
print(agemax)

# en fazla maaş alanı bulalım
# her departmanda en az maas alan  maası
salarymax=df.groupby("Departman")["maas"].min()["muhasebe"]# eger muhasebeyi eklersek sadece 
                                                           #muhasebenin degerini ekrana yazdırtmış oluyoruz
print(salarymax)

# hesapla işlemlerimiz için agg metodunuda kullanabiliriz

result=df.groupby("Departman").agg(np.mean) # burda ise departmandaki ortalama degerleri bulmamızı saglıyor
print(result)

# agg kullanmamızın sebebi orda onunla daha fazla işlem yapma şansımızın olmasıdır

result=df.groupby("Departman")["maas"].agg([np.mean,np.sum,np.max,np.min])
print(result)


result=df.groupby("Departman")["maas"].agg([np.mean,np.sum,np.max,np.min]).loc["muhasebe"]
print(result)
# burda ise sadece muhasebe için olanları ortaya koymamızı saglıyor


