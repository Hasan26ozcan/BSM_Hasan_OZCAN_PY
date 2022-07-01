def notları_hesapla(satır):
    toplam=0
    satır=satır[:-1]
    print(satır)
    liste=satır.split(":")
    ogreciadi=liste[0]
    notlar=liste[1]
    listes=notlar.split(",")
    print(listes)
    for i in listes:
        toplam=toplam+int(i)
    ortalama=toplam/3
    if(ortalama>=90):
        harf="AA"
    elif(ortalama>=85 and ortalama<=89):
        harf="BA"
    elif(ortalama>=65):
        harf="CC"
    else:
        harf="FF"
    return ogreciadi+": "+str(ortalama) +"harf sistemindeki karşılıgı: "+str(harf)


def ortalama_oku():
    with open("sınavnotları.txt","r",encoding="utf-8") as find:
        for satir in find:
            print(notları_hesapla(satir))
def not_gir():
    ad=input("adınızı giriniz:")
    soyad= input("soyadınızı giriniz: ")
    not1=input("not 1:")
    not2=input("not 2:")
    not3=input("not 3:")
    with open("sınavnotları.txt","a",encoding="utf-8") as find:
        find.write(ad+" "+soyad +" notlar:"+not1+","+not2+","+not3+"\n")


def not_kaydet():
    with open("sınavnotları.txt","r",encoding="utf-8") as find:
        list=[]
        for satir in find:
            list.append(notları_hesapla(satir))
        with open("sınavkayıt.txt","w",encoding="utf-8") as finds:
            print(list)
            for i in list:
                finds.write(str(i)+"\n")
    with open("sınavnotları.txt","r",encoding="utf-8") as find:
        print(find.read())


    













while( True):
    print("1- oratalama oku\n2- not gir\n3-notları kaydet\n4-çıkış")
    islem =input()
    if ("1"==islem):
        ortalama_oku()
    elif("2"== islem):
        not_gir()
    elif("3"== islem):
        not_kaydet()
    elif("4"==islem):
        break
    else:
        print("yanlış deger girdiniz")
        break