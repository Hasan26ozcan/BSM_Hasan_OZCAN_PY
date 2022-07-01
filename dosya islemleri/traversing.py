file =open("newfile2.txt","r",encoding= "utf-8")



print(file.read())
file.close()
# bi şuana kadar böyle yapıyorduk ve açtıgımız dosyayı kapatmamız gerekiyordu

print("**"*50)
with open("newfile2.txt","r",encoding= "utf-8") as file : # burda as dediğimizde saoldakinden çıkan degeri sağdaki degere atıyor
    print(file.read(10))
    file.seek(0) #burada ise bu imlecimizin nereye gitmesini istedigimizi söylüyoruz
    print(file.tell())#bu fonksiyon bizim tell imiz yani imlecimizin nerede odlugunu söylüyor
    print(file.read(10))





