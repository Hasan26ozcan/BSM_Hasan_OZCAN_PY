liste=["1","2","5a","10b","abc","10","50"]
#1:liste elemanları içindeki sayısal degerleri bulunuz
lis=[]
for x in liste:
    try:
        #try ya yapılan işlemde eğer bir hata yapıldıysa eğer except olan yere giriyor ve
        #ordan çıkan degere göre de hataya gönderiyor eger hata yoksa da except else if else yapısı gibi
        #hata yoksa else giriyor
        x=int(x)
    except Exception as a:
        print(f"hatalı {x} ",a)
    else:
        lis.append(x)
print(lis)

#2:kullanıcıdan q degeri girmedikçe aldıgınız inputun sayı
# oldugundan emin olunuz aksi halde hata mesajı yazın
inputa=input("degerinizi giriniz:")
listesi=[]
counter=1
while("q"!= inputa):
    try:
        inputa=int(inputa)
    except Exception as a:
        print(f"hatalı islem yapıldı {inputa} ",a)
    else:
        listesi.append(x)
    finally:
        print(f"{counter}. islem bitti")

    inputa=input("degerinizi giriniz:")
    print(inputa)
    counter+=1






#3:girilen parola içinde türkçe karakter hatası veriniz
psw=input("parolanızı giriniz: ")
import re

if(re.search("[ğ, Ğ, ç, Ç, ş, Ş, ü, Ü, ö, Ö, ı, İ]",psw)):
    raise Exception("türkçe karakter kullanılmıştır")
else:
    print("hiç bir sorun yok")

    





#4 faktoriyel fonksiyonu oluşturp fonksiyona gelen deger için hata mesajı verin
######
# negatif bir sayıysa ve sayıya çevrilemeyen birşeyse hata verelim

sayi=input("sayinizi giriniz: ")

def fuonksiyon(sayi):
    try:
        control2(sayi)
        sayi=int(sayi)
        control(sayi)
    except Exception as a :
        print(a)
    else:
        faktoriyeli=1
        for a in range(1,sayi+1):
            faktoriyeli=faktoriyeli*a
    finally:
        print("islemimiz bitmistir")
    
    print(faktoriyeli)

def control(sayi):
    if(sayi<0):
        raise Exception("sayimiz negatif oldugu için islem yapılamıyor")
def control2(sayi):
    try:
        sayi=int(sayi)
    except Exception:
        raise Exception("bu bir sayi değildir")




print(fuonksiyon(sayi))






