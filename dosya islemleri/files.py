#dosya açmak ve oluşturmak için open() fonksiyonu kullanılır
# kullanımı : open(dosya_adi,dosyaya erişme modu)
#dosya _erişme_modu => dosyayı hangi amaçla açtığımızı belirtir


# "w": (write) yazma modu.dosyayı konumda oluşturur
#       dosyayı konumunda oluşturur 
#       eski den yazan herşeyi sıfırlar ve kendi yazdığını koyar

result= open("newfile.txt","w")
result.close()

file =open("C:/Users/Hasan Özcan/Desktop/newsfile.txt","w")
print(file)

file.close()


result=open("newfile.txt","w",encoding="utf-8")
result.write("hasan özcan")
result.close()

# "a": (append) ekleme. dosya konumunda yoksa oluşturur
# burda ise bize 


file =open("newfile.txt","a",encoding="utf-8")
file.write("\nbilgisayar mühendisliği\n")
file.write("\ncomputer\n")
file.close()
# "x": (create) oluşturma. dosya zaten varsa hata verir
#sadece dosya oluşturmak istersek eger burayı kullanabiliriz
file =open("newfile2.txt","x")
print(file)




# "r": (read) okuma.varsayılan.dosya konumunda yoksa hata verir









    




