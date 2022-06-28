#1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyon kodunu yazınız
kelimeniz=input("kelimenizi giriniz: ")
tekrar=int(input("kaç kez ekrana yazılsın: "))
def screanwrite(tekrar,kelimemmiz):
    counter=0
    while(counter<tekrar):
        print(kelimemmiz)
        counter+=1
screanwrite(tekrar,kelimeniz)

def ekranayazdırma(kelime,tekrar):
    print(f"{kelime}\n"*tekrar)

ekranayazdırma(kelimeniz,tekrar)

#2- Kendine gönderilen sınırsız sayidaki parametreyi bir listeye çeviren fonksiyonu yazınız
def funcpara(*liste):
    listemiz=[]
    for x in liste:
        listemiz.append(x)
    return listemiz

liste=funcpara(12,3,4,5,6,2,3,21,23,"merhaba","sadık","merhaba",4,21,23,4)
print(liste)
#3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun
sayi1=int(input("birinci sayınızı giriniz: "))
sayi2=int(input("ikinci sayinizi giriniz: "))

def sayıaralığı(sayi1,sayi2):
    if(sayi1<sayi2):
        listesi=[]
        while (sayi1<sayi2+1):
            if(asalsayimi(sayi1)):
                listesi.append(sayi1)
            sayi1+=1
        return listesi
    elif(sayi2<sayi1):
        listesi=[]
        while (1+sayi1>sayi2):
            if(asalsayimi(sayi2)):
                listesi.append(sayi2)
            sayi2+=1
        return listesi
    else:
        return "başlangıç bitiş aynı sayı olamaz "

    


def asalsayimi(sayi):
    counter=1
    control=0
    while(counter<=sayi):
        if(sayi%counter==0):
            control+=1
        counter+=1
    if(control==2):
        return True
    else:
        return False    

listemiz=sayıaralığı(sayi1,sayi2)
print(listemiz)
for x in listemiz:
    print(x)







#4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürün
sayimiz=int(input("sayımızı gönderelim: "))

def sayımızıntambölenleri(sayimiz):
    listemiz=[]
    count=1
    while(count<=sayimiz):
        if(sayimiz%count==0):
            listemiz.append(count)
        count+=1
    return listemiz

liste=sayımızıntambölenleri(sayimiz)
print(liste)

        





