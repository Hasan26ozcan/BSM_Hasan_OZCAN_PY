website="http://www.sadikturan.com"
course="Python kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
#1- course karakter dizisinde kaçkarakter bulunmaktadır ?

#2- website içinden www karakterini alın.

#3- website içinden com karakterini alın.

#4- course içindeki ilk 15 ve son 15 karakterini alınız

#5 course ifadesindeki karakterleri tersten yazdırın

print(len(course))
print(website[7:10])
print(website[len(website)-3:len(website)])
print(course[:15])
print(course[len(course)-15:len(course)])
print(course[::-1])# iki nokta 2 tane olması bütün karakterleri ala ve -1 den sonuna kadar
#1 dersek bütün karakterleri al - dersek ise soldan sağa değil sağdan sola diyoruz yani normal 2:40:3 de yaptığımızla 
#işlevi yapıyor sadece ilk sen son değerleri yazmadık diye onuda şöyle yapabiliriz
print(course[len(course)-1::-1])
#yani burdada gözüktügü gibi baslama yerimiz son deger bitis degerimiz sayının kendisi 0. indeks ama yazarsak onu almaz

name,surname,age,job="Bora","Yılmaz",32,"Mühendis"

#6- yukarıda verilen değişkenler ,lke ekrana aşağıdaki ifadeyi yazdırın.
#      Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis

print("Benim adım {} {}, Yaşım {} ve mesleğim {} ".format(name,surname,age,job))
print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job} ")
#7- Hello world ifadesindeki "w" yerine W harfiyle değiştiriniz

a="Hello world"
s=a[0:6]+"W"+a[7:len(a)]
print(s)
# s.replace dediğimiz metotlada w gördüğün yere W koy diyebiliriz işimizi kolaylaştırır
# "abc" ifadesini yan yana üç kere yazdırın
s="abc "*3
print(s)





