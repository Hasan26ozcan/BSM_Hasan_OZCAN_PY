x,y,z =2,5,10
numbers =1,5,7,10,6
#1- kullanıcıdan aldığımız 2 sayının çarpımı ile x,y,z toplamının farkı nedir
sayi1= float(input("birinci sayınızı giriniz: "))
sayi2= float(input("ikinci sayınızı giriniz: "))
sum1=sayi1*sayi2
sum2=x+y+z
sum= sum1-sum2
print(sum)
#2- y'nin x 'e kalansız bölümünü hesaplayınız
bol= y //x
print(bol)
#3- (x,y,z) toplamının mod 3'ü nedir
mods=(x+y+z)%3
#4- y' nin x. kuvvetini hesaplayınız
us=y**x
print(us)
#5- x,*y,z =numbers işlemine göre z' nin küpü kaçtır 
x,*y,z=numbers
print(z)
coun=z**3
print(coun)
#6- x,*y,z = numbers işlemine göre y nindeğerleri toplamı kaçtır
x,*y,z=numbers
print(y)
print(len(y))
suma=y[0]+y[1]+y[2]
print(suma)
