#1- Girilen bir sayının 0-100 arasında olup olmadğını kontrol ediniz

sayi1 =float(input("bir sayı giriniz aralığına bakalım: "))
bol= (sayi1<100) and (sayi1>0)
print(f"girilen sayımız 0 ve 100 aralığındamıdır {bol} ")
#2- Girilen bir sayının pozitif çift sayi olup olmadığını kontrol ediniz
sayi1 =float(input("bir sayı giriniz pozitif çift olup olmadığına bakalım: "))
bol=(sayi1>0) and (sayi1 %2==0)
print(bol)
#3- Email ve parola bilgileri ile giriş kontrolü yapınız
Email ="email@sadikturan"
parola ="abc123"
emaili=input("email adresini giriniz:")
parolası=input("parolasını giriniz: ")
bol=(emaili==Email)
bole=(parola ==parolası)
bolem=(emaili==Email) and (parola ==parolası)
print(f"email adresi doğrumu: {bol} \nparolası doğrumu: {bole}  \ngiriş yapılmıştır: {bolem} ")
#4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız
sayi1=float(input("Birinci sayiyi giriniz: "))
sayi2=float(input("İkini sayiyi giriniz: "))
sayi3=float(input("Üçüncü sayiyi giriniz: "))
print("*"*60)
bol1=(sayi1<sayi2) and (sayi1<sayi3)
print(f"en küçük sayı sayi1 midir {bol1} ")
bol2=(sayi2<sayi3) and (sayi2<sayi1)
print(f"en küçük sayı sayi2 midir {bol2} ")
bol3=(sayi3<sayi1) and (sayi3<sayi2)
print(f"en küçük sayı sayi3 midir {bol3} ")

bol1=(sayi1>sayi2) and (sayi1>sayi3)
print(f"en büyük sayı sayi1 midir {bol1} ")
bol2=(sayi2>sayi3) and (sayi2>sayi1)
print(f"en büyük sayı sayi2 midir {bol2} ")
bol3=(sayi3>sayi1) and (sayi3>sayi2)
print(f"en büyük sayı sayi3 midir {bol3} ")



















print("*"*60)
bol1=(sayi1<sayi2)
bol2=(sayi1<sayi3)
results=(sayi1<sayi2) and (sayi1<sayi3)
print(f"en küçük sayı sayi1 dir {results} ")
bol3=(sayi2<sayi3)
ortanca = (results==True) and (bol3 ==True)
print(f"en büyük sayi sayi3 tür: {bol3} " )
print(f"ortanca sayı sayi2 dir {ortanca} ")
print(f"sayi1 < sayi2 {bol1} \n sayi1<sayi3 {bol2} \nsayi2<sayi3 {bol3} ")
#5- Kullanıcıdan 2 vize (%60) ve final (%40) notu alığ ortalama hesaplayınız
#   Eğer ortalama 50 ve üstüyse geçti değilse kaldı 
#   a-) ortalama 50 olsa bile final notu en az 50 olmalıdır
#   b-) finalden 70 aldığında ortalamanın önemi olmasın
sayi1=float(input("1. vize notunu giriniz: "))
sayi2=float(input("2. vize notunu giriniz: "))
sayi3=float(input("final notunu giriniz: "))
sum=((sayi1*0.6)+(sayi2*0.6))/2+(sayi3*0.4)
bol=(sum>=50)
print(f"bu dersten geçilmişmidir {bol} ")
bolm=(sum==50) and ( sayi3>=50)
print(f"ortalama 50 mi {bol} {sum} bu dersten geçilmişmidir {bolm}")
bole=(sayi3>=70) or (sum>=50)
print(f"not 70 ve üzeri mi {bole} ortalaması {sum} dersten geçme durumu {bole} ")
print("**"*40)

result= (sum >=50) and (sayi3>=50)
print(f"ortalama {sum} final notu {sayi3} dersten geçme durumu {result}")
result= (sum >=50) or (sayi3>=70)
print(f"ortalama {sum} final notu {sayi3} dersten geçme durumu {result}")


print("**"*40)
#6-kişinin ad,Kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız
#  Formül: (kilo/boy uzunluğu karesi) 
#  Aşağıdaki tabloya göre kişi hangi gruba girmektedi 
#   0-18.4   =>zayıf
#   18.5-24.9=>Normal
#   25.0-29.9=>Fazla kilolu
#   30.0-34.9=>Obez
name=input("kişinin adınız giriniz: ")
weight = float(input("kişinin kilosunu giriniz: "))
lange =float(input("boy uzunluğunu giriniz: "))

form=(weight/lange**2)
bool1=(form>0) and (form<=18.4)
bool2=(form>18.4) and (form<= 24.9)
bool3=(form >=25.0) and (form <=29.9)
bool4=(form >=30.0) and (form <=34.9)
print(f"Zayıf kategorisindemi: {bool1} ")
print(f"Normal kategorisindemi: {bool2} ")
print(f"Fazla kilolu kategorisindemi: {bool3} ")
print(f"Obez kategorisindemi: {bool4} ")

