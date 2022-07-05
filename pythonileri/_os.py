import os
import datetime




print(dir(os))
print(os.name)
print(os.getcwd())

# burada yapılan şey klasöt oluturma
#print(os.mkdir("ahmetnerede"))


#dizinimizde güncelleme yapmak
# os.chdir("c:/")
#print(os.chdir("../.."))


#dizimizin yerine ögrenmek
print(os.getcwd())


#burada olan islem ise iç içer dosya açmamızı sağlayan bir sistem
#os.makedirs("asdasd/new directors/newsayi/asd")

print(os.listdir("c://"))

print("**"*50)
for dosya in os.listdir():
    print(dosya)
    print(dosya.endswith(".py"))

#mesela şimdi sadece py ile bitenleri ekrana yazdıralım

for dosya in os.listdir():
    if dosya.endswith(".py"):
        print(dosya)
print("**"*70)
#bir dosya hakkında bilgi sahibi olmak istersek eger 
result1= os.stat("if-else.py")
length= result1.st_size/1024
print(length)
start= result1.st_ctime #il oluşturulma tarihi
end=result1.st_atime # son erişilme tarihi
mid=result1.st_mtime # değiştirilme tarihi
#datetime clası üzerinden datetime mdülü üzerine geçiş yapıyoruz
datetime.datetime.fromtimestamp(start)
datetime.datetime.fromtimestamp(end)
time=end-start
print(time)




print(result1)

#os.system("notepad.exe")
#os.chdir("c:/")
#os.rename("newdirector","yenklasör")
print(os.getcwd())
print("****")
# os.rmdir("newdirector")
# os.removedirs("yeniklasor/yeniklasor")

# path daha çok uzantıda kullandığımız birşey


print(os.path.abspath("_os.py")) #bize tam konumunu verdi
print(os.path.dirname("C:/Users/Hasan Özcan/Desktop/python_temelleri/_os.py"))# tam konumu verilen dosyanın dizin ismini alıyoruz
#aslında söyle elimizde bir dpsya var ve bu dosyanın dizini bize gerek işte o zaman bunu kullaniliyoruz
print(os.path.dirname(os.path.abspath("_os.py")))
#exixt ise sorgulama olarak söyleyebiliriz

print(os.path.exists("C:/Users/Hasan Özcan/Desktop/python"))#böyle bir dosya varmı konumunu verek öğrenebiliriz ya da
#onu çalıştırmak istdiğimiz yere getirip ordada kontrol edebiliriz

#ulaştıgımız şeyin klasör olup olmadığına bir bakalım
print(os.path.isdir("C:/Users/Hasan Özcan/Desktop/python"))
print(os.path.isfile(os.path.abspath("_os.py")))# ulaştıgımız dizin dosyamı dizinmi bunu sorgulamaya yaarıyor


#birleştirme işlemi yaparken 
print(os.path.join("C:","DENEME","DENEME"))
print(os.path.split("C:/DENEME"))
print(os.path.splitext("_os.py"))#burda ismiyle uzantısını ayırmasını sağlıyor
#elimizde bir resim va ve resimin adını değiştirmke istiyoruz yada ismi aynı kalsın ama uzantısını değiştirmek istiyoruz
#işte tamda burada devreye bu giriyor
result=os.path.splitext("_os.py")
print(result[0])
print(result[1])
print(result[0])
print(os.path.join(result[0]+"  ","   "+result[1]))

liste=[1,2,3,4,5,6]
liste[0]=123
print(liste[0])



