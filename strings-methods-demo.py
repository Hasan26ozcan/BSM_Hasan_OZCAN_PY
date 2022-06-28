Website="http://www.sadikturan.com"
course="Python Kursu: Baştan Sona Python Programlama Rehberinizi (40 saat)"

#1- " Hello World " karakter dizisinin baş ve sondakş boşluk karakterini silin
write="Hello World"
write=write.strip()
print(write)
print(len(write))

#2- "www.sadikturan.com" içindeki sadikturan bilgisi haricindeki her karakteri silin
a ="http://www.sadikturan.com"
a=a.lstrip("http://")# başına l ya da r koymamız hangi taraftan silmek istediğimiz söylemiş oluyoruz
# sol taraftan hangi harflerin silinmesini istiyorsak onları yazıyoruz
a=a.strip("www..com")
print(a)

#3- "course" karakter dizisinin tüm karakterlerini küçük harf yapın
course=course.lower()
print(course)
course="Python Kursu: Baştan Sona Python Programlama Rehberinizi (40 saat)"
#4- "website" içerisinde kaç tane a karakteri vardir
indeks = Website.count("a")
print(indeks)

#5- "website" www ile başlayıp com ile bitiyormu

start= Website.startswith("www")
finish= Website.endswith("com")
print("www başlama sonucu: {} com ile bitme sonucu: {} ".format(start,finish))

#6- "website" içinde ".com" ifadesi var mı

indekse= Website.find(".com")
bol=indekse !=-1
print(indekse)
print(bol)
print(course)
result=course.rfind("Python")
print(result)
result=Website.index(".com")
print(result)
#result=Website.rindex(".comm")#exception
print(result)
#7- "course" içindeki karakterlerin hepsi alfabetikmi
course=course.split()
print(course)
print(len(course))
bola= str(course[0]).isalpha()
print(bol)
bol= str(course[1]).isalpha()
print(bol)
bol= str(course[2]).isalpha()
print(bol)
bol= str(course[3]).isalpha()
print(bol)
bol=str(course[4]).isalpha()
print(bol)
bol=str(course[5]).isalpha()
print(bol)
bol= str(course[6]).isalpha()
print(bol)
bol= str(course[7]).isdigit()
print(bol)
bol= str(course[8]).isalpha()
print(bol)
#8- "contents" ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz
a ="contents"
b="contents"
c="contents"
a=a.center(50,"*")
print(a)
b=b.ljust(50,"*")
print(b)
c=c.rjust(50,"*")
print(c)

#9- "course" karakter dizisindeki tüm boşluk karakterlerini "-" ile değiştirin
course=" ".join(course)
course= course.replace(" ","-")
print(course)

#10- "Hello World" karakter dizisinin "World" ifadesini "There" olarak değiştir
abc="Hello World"
abc=abc.replace("World","There")
print(abc)

#11- "course" karakter dizisinin boşluk karakterlerinden ayırın
course=course.replace("-"," ")
print(course)
course=course.split()
print(course)