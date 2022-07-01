

try:
    file =open("newfile.txt","r")
    print(file)
except Exception:
    print("dosya okuma hatası")
finally:
    print("dosya kapandı")
    file.close()
print("**"*50)


file =open("newfile.txt","r",encoding="utf-8")
#for döngüsü
for i in file:
    print(i)
file =open("newfile.txt","r",encoding="utf-8")
for i in file:
    print(i,end="")
    #bu islemde ise araya bosluk bırakmadan alt alta yazma islemi yapılır

#read() fonksiyonu ile yapabiliriz
file =open("newfile.txt","r",encoding="utf-8")

content1= file.read()
print("\niçerik1")
print(content1)

file =open("newfile.txt","r",encoding="utf-8")

content2=file.read()
print("içerik2")
print(content2)
print("**"*100)
file =open("newfile.txt","r",encoding="utf-8")
content=file.read(10)# eger boyle yapar isek burada bize ilk 10 karakteri veriyor
content=file.read(10)

print((content))
file =open("newfile.txt","r",encoding="utf-8")


#readline
#bize ise burda ilk satırı okumasını saglıyor
print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),)
print(file.readline(),)
print(file.readline(),)
print(file.readline(),)
print(file.readline(),)

##readlines metotdunu kullanalım
file =open("newfile.txt","r",encoding="utf-8")

contents= file.readlines()
print(contents)
print(contents[0])
print(contents[1])
print(contents[2])
print(contents[3])

