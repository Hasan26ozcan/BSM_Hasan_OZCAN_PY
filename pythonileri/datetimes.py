from datetime import timedelta, datetime
# from datetime import date
# from datetime import time
#import datetime
# böyle yaptğımızda tek bir modülün importunu aşıyoruz



#from datetime import datetime


simdi=datetime.now()
result=datetime.today()

#aslınd abuda now ve today islevlerinde yapılan islem


print(result.date())
print(result.time())
print(result.second)
print(result.month)
print(result.hour)
print(result.minute)
print(result.second)
# bize o günün tarihini daha açıklayıcı bir şekilde veriyor
print(datetime.ctime(result))
print(datetime.strftime(result,"%Y")) #küçük y yıın son 2 rakamını alıyor büyük y ise hepsini alıyor
print(datetime.strftime(result,"%B"))
print(datetime.strftime(result,"%D"))
print(datetime.strftime(result,"%A"))
print(datetime.strftime(result,"%X"))
print(datetime.strftime(result,"%Y %B  %A "  ))

print("**"*50)


t="21 nisan 2019"
gün ,ay,yil=t.split()
print(gün)
print(ay)
print(yil)


t="15 February 2022 hour 10:02:18"
                    #     15 nisan 2022 hour 10:02:18
st= datetime.strptime(t,"%d %B %Y hour %H:%M:%S")
print(st)
# burdan farklı bir durum oalrak ayı inglizce girmemiz gerekiyor


print("**"*50)
print(dir(datetime))
print(datetime.now().time())
print("sa")


sayi=datetime(2003,2,13,12,32,1,9)
print(sayi)

saf=datetime.timestamp(sayi)#burda verilen tarhi bilgisini saniye bilgisine çevirir
print(saf)

saft= datetime.fromtimestamp(saf)# burdada verilen saniyeyi tarihe çevirir
print(saft)

sfata=datetime.fromtimestamp(0)
print(sfata)
#burda ise gödügümüz deger bilgisayarın dogum tarihi olarak geçiyor ve eger bir şeyi saniyeye çeviriceksek
#ve o tarihi bu tarihten çıkartarak saniyeye çeviriyor


simdi=datetime.now()
time=simdi-sayi
print(time)
print(time.days)
print(time.microseconds)


result = simdi + timedelta(days=10,minutes=100)
print(simdi)
print(result)
# burada oldugu gibi üzerine on gün ekledik

print("&&&"*50)
result1=simdi-timedelta(days=10,seconds=100)
print(simdi)
print(result1)


