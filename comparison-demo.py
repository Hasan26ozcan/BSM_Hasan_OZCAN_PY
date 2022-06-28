
#1- Girilen 2 sayıdan hangisi büyüktür
sayi1= float(input("1. sayıyı giriniz: "))
sayi2= float(input("2. sayıyı giriniz: "))
# if(sayi1>sayi2):{
#     print(f" {sayi1} daha büyüktür ")
# }
# else:{
#     print(f" {sayi2} daha büyüktür ")
# }
bol=sayi1>sayi2
print(f"a: {sayi1} ,b {sayi2} a b den büyükmüdür {bol} ")


#2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
#  Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın
sayi1= float(input("vize notunuzu giriniz:  "))
sayi2= float(input("vize notunuzu giriniz:  "))
sayi3= float(input("final notunuzu giriniz: "))
sayi1=(sayi1*60)/100
sayi2=(sayi2*60)/100
sayi3=(sayi3*40)/100
sum=(sayi1+sayi2)/2+sayi3
# if(sum>=50):{
#     print(f" geçti ve notu {sum} " )
# }
# else:{
#     print(f"kaldı ve botu {sum} ")
# }
bol = (sum>=50)
print(f"dersten geçtimi {bol} not ortalaması {sum} ")

#3- Girilen bir sayının tek mi çift mi olduğunu yazdırın
sayi1= float(input("bir sayi giriniz tek çift giriniz: "))
# if(sayi1%2==1):{
#     print(f"tek sayıdır sayi {sayi1} ")
# }
# else:{
#     print(f"çift sayıdır sayi {sayi1} ")
# }
bol= (sayi1%2==1)
print(f"sayı tek sayımıdır: {bol} ")
#4- Girilen bir sayının negatif pozitif durumunu yazdırın
sayi1= float(input("negatif ya da pozitif sayıyı giriniz: "))
# if(sayi1>0):{
#     print(sayi1)
# }
# else:{
#     print(sayi1*-1)
# }
bol = sayi1>=0
print(f"girilen sayi pozitif midir {bol} ")



#5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz
email ="email@sadikturan.com" 
paralo ="abc123"
emaili= input("eposta değerinizi giriniz: ")
password= input("parola değerinizi giriniz: ")
emaili= emaili.strip().lower()
password=password.strip().lower()

emailcorrect=(emaili == email)
passwordscorrect=(password== paralo)
print(f"email bilgisi doğrumu :  {emailcorrect}  parola bilgisi doğrumu : {passwordscorrect}")


# if(emaili == email):
#    if(password== paralo):{
#     print("sisteme giriş başarılı")


#    }