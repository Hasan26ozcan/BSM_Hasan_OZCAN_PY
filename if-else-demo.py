#1- kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme
#   durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu
#   lise ya da üniversite olmalıdır
import datetime



name=input("isminizi giriniz: ") 
age=float(input("yaşınızı giriniz: "))
scholl=input("eğitim durumunuzu giriniz: ")
if (age >= 18) and ((scholl=="lise") or (scholl=="üniversite")):
    print("ehliyet alabilirsiniz")
elif (age >= 18) or ((scholl=="lise") or (scholl=="üniversite")):
    if(age >= 18): 
        print("eğitim bilginiz yetersiz maalesef ehliyet alamazsınız")
    else:
        print("yaşınız tutmuyor eliyet alamazsınız")
else :
    print("hiçbir özelliğiniz tutmuyor maalesef")





#2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
#   not aralığınına karşılık gelen not bilgisini yazdırın
#   0 -24  => 0
#   25-44  => 1
#   45-54  => 2
#   55-69  => 3
#   70-84  => 4
#   85-100 => 5
sınav1=float(input("1. yazılı notunuzu giriniz: "))
sınav2=float(input("2. yazılı notunuzu giriniz: "))
sözlü=float(input("sözlü notunuzu giriniz: "))

sum= (sınav1+sınav2+sözlü)/3
print("5 lik sisteme göre notunuz")
if(sum>0 and sum<=24):
    print( f"ortalamanız {sum} 0")
elif(sum>=25 and sum<=44):
    print( f"ortalamanız {sum} 1")
elif(sum>=45 and sum<=54):
    print( f"ortalamanız {sum} 2")
elif(sum>=55 and sum<=69):
    print( f"ortalamanız {sum} 3")
elif(sum>=70 and sum<=84):
    print( f"ortalamanız {sum} 4")
elif(sum>=85 and sum<=100):
    print( f"ortalamanız {sum} 5")
else:
    print("yanlış notlandırma yaptınız")




#3- Trafiğe çıkış tarihini alınan bir aracın servis zamanını aşağıdakii bilgilere göre hesaplayınız
#   1. bakım =>1.yıl
#   2. bakım =>2.yıl
#   3. bakım =>3.yıl
#   **Süre hesabını alınan gün,ay,yıl bilgisine göre gün bazında hesaplayınız
#   *** datatime modülünü kullanmamız gerekiyor
days =float(input("aracınız kaç gündür trafikte"))
if (days<=365):
    print("1.bakım")
elif((days>=365) and (days<=365*2)):
    print('2. bakım')
elif((days>365*2) and (days<=365*3) ):
    print("3. bakım")
else :
    print("bakım yeri dolmuştur")





tarih=input("aracın çıkış tarihini giriniz: gün.ay.yıl olacak şekilde aralarına '.' koyarak yazınız:  ")
tarih=tarih.split(".")
günümüztarihi ="19.6.2022"
x= datetime.datetime.now()
y= datetime.datetime(int(tarih[2]),int(tarih[1]),int(tarih[0]))
print(x)
print(y)
a= (x-y)
print(a.days)
a=a.days

if (a<=365):
    print("1.bakım")
elif((a>=365) and (a<=365*2)):
    print('2. bakım')
elif((a>365*2) and (a<=365*3) ):
    print("3. bakım")
else :
    print("bakım yeri dolmuştur")



