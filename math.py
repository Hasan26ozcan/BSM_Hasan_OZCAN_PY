#hazır bir modül kullanalım
# modullerin asıl amacı yapilacak olan isim parcalanmasi bu sayade guncelleme ya da baska birsey oldugunda daha kolay
#islem yapılmasini saglar
import math
import math as islem # eger boyle birsey yaparsak biz meth modulune takma ad vermis oluyoruz
# islem math de olan herseyi kullanıyor
print("para")
#print(dir(math))
# value=help(math.factorial(24))

# print(value)
# bu islemle math modulu icerisndeki butun bilesenleri yazdırırız

# print(math.sqrt(64))
# print(math.fabs(-50))

print(islem.sqrt(49))
print(islem.factorial(5))
print(islem.sin(90))
print(islem.floor(6.9))
print(islem.ceil(5.1))



from math import * # ilgili moduldeki hersey import edilmis oluyor
# ilgili fromdan import et hepsini demek oluyor bu
# boyle yaptıgımızda math ya da islem yazmamıza gerek yok direkt olarak yazabiliriz
def sqrt(x):
    print("x: ",x)

value=factorial(5)
print(value)

val=sqrt(121)#sonrasinda tanimlanan hangisiyse onu kullaniyor
print(val)

from math import factorial,sqrt # burda ise sadece bunlari kullanicagimizi soyluyoruz

