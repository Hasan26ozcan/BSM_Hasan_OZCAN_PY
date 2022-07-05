import requests
import json

rest=requests.get("https://api.genelpara.com/embed/doviz.json")
print(rest)
rest=rest.text

jsons= json.loads(rest)


for a in jsons:
    print(a)


deger=input("islem yapmak istediginiz deger")
deger=deger.upper()
islem=int(input("alıs yapmak istiyorsanız 1\nsatıs yapmak istiyorsanı 2 tusuna basınız ")) 
print(jsons[deger]["alis"])
print(jsons[deger]["degisim"])
toplam=float(jsons[deger]["alis"])+float(jsons[deger]["degisim"])




print(toplam)
if(islem==1):
    paramiktarı=float(input("para miktarınızı giriniz: "))
    degeri=float(jsons[deger]["alis"])
    alınanmiktar= paramiktarı/degeri
    print(alınanmiktar)


elif(islem==2):
    for a in jsons:
        print(a)
    cevrilendeger=input("degere bozdurmak istiyorsunuz")
    cevrilendeger=cevrilendeger.upper()
    bozdurulacakdeger=float(input(f"kaç {deger} bozdukmak istiyorsunuz: "))
    toplam=float(jsons[deger]["alis"])+float(jsons[deger]["degisim"])
    toplampara=bozdurulacakdeger*toplam
    cevirilenparadegeri=toplampara/float(jsons[cevrilendeger]["alis"])
    print(f" {cevrilendeger} de degeri {cevirilenparadegeri} ")

    
    
    
    jsons[cevrilendeger]















