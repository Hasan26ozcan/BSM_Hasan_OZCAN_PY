#1- girilen sayı 0 ile 100 arasında olup olmadığını kontrol ediniz
sayi =float(input("sayınızı giriniz 0 - 100 aralığında olup olmadığına bakalım: "))
if (sayi <100 and sayi>0):
    print("sayımız 0 ve 100 arasındadır")

#2- girilen bir sayının pozitif çift sayı olduğunu bulunuz
sayi =float(input("pozitif çift sayı olup olmadığına bakalım"))
if( sayi>0 ): 
    if(sayi%2==0):
        print("sayi pozitif ve çift sayı")
    else:
        print("pozitif ve tek sayıdır")    
elif(sayi<0) :
    if (sayi%2 ==0 ):
        print("sayi negatif ama çift sayı")
    else:
        print("sayı negatif ve tek sayı")
else:
    print("sayımız 0 dır")
#3- Email ve parola bilgileri ile giriş kontrolü yapınız
email ="email@sadikturan.com"
password ="abc123"

girilenemail=input("email adresinizi giriniz: ")
girilenpassword=input("passwordunuzu giriniz: ")

if(email==girilenemail and password== girilenpassword):
    print("sisteme giriş başarılı bir şekilde gerçekleşmiştir")
else:    
    if (email == girilenemail ):
        print("şifrenizi yanlış girdiniz")
    elif(password == girilenpassword) :
        print("email adresinizi yanlış girdiniz:")    
    else:    
        print("email ve şifreniz yanlış")
#4- girilen 3 sayıyı büyüklük olarak karşılaştırınız
sayi1=float(input("sayi1: ")) 
sayi2=float(input("sayi2: "))
sayi3=float(input("sayi3: "))

if(sayi1>sayi2 and sayi1>sayi3):
    print(f"en büyük sayı {sayi1} dir ")
elif(sayi2>sayi1 and sayi2>sayi3):
    print(f"en büyük sayı {sayi2} dir ")
else:
    print(f"en büyük sayı {sayi3} dir ")
#5- kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp alıp ortalama hesaplayınız:
#   Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#   a-) Ortalama 50 olsa bile final botu en az 50 olmalıdır
#   b-) finalden 70 alındığında ortalamanın bir önemi olmasın
vize1=float(input("1. vize notunuzu giriniz:"))
vize2=float(input("2. vize notunuzu giriniz: "))
final=float(input("final notunuzu giriniz: "))
sum=((vize1*0.6 +vize2*0.6)/2+final*0.4)
if(sum>=50 and final >= 50):
    print(f"dersten geçtiniz ortalamanız {sum} final notunuz {final}  ")
elif(final>=70 or sum>=50):
    print(f"dersten geçtiniz: ortalamanız {sum} final notunuz {final} ")    
else:
    print("dersten kaldınız")

print("**"*50)
if(sum>=50 and final>=50):
    print("dersten geçtiniz: ")
elif(final>=70):
    print("derstenn geçtiniz:")
elif(sum>=50):
    print("dersten geçtiniz:")
else:
    print("dersten kaldınız")    




print("**"*50)
#6- Kişinin ad,kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız
#   Formül (Kilo /boy uzunluğunun karesi)
#   Aşağıdaki tabloya göre kişi hangi gruba girmektedi
#   0-18.4    =>Zayıf    
#   18.5-24.9 =>Normal
#   25.0-29.9 =>Fazla kilolu
#   30.0-34.0 =>Şişman (obez)

name= input("adınızı giriniz: ") 
weigth= float(input("kilonuzu giriniz: "))
long= float(input("boy bilginizi giriniz: "))

form=(weigth/long**2)

if(form>=0 and form<=18.4):
    print(f" {name} durumu zayıf ")
elif(form>=18.5 and form<=24.9):
    print(f" {name} durumu Normal ")
elif(form>=25.0 and form<=29.9):
    print(f" {name} durumu Fazla kilolu ")
elif(form>=30.0 and form<=form+1):
    print(f" {name} durumu Şişman (Obez) ")
else:
    print("yanlış değerler girdiniz")
