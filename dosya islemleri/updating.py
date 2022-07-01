with open("newfile.txt","r+",encoding="utf-8") as file:
    print(file.read())
#r+ hem okuma hemde yazma modunu temsil ediyor
with open("newfile.txt","r+",encoding="utf-8") as file:
    print(file.write("deneme"))

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     print(file.read())
#     print(file.write("\nahmet çakar"))


with open("newfile.txt","r+",encoding="utf-8") as file:
    print(file.read())
#sayfa soununda güncelleme
with open("newfile.txt","a",encoding="utf-8") as file:
    file.write("\nahmet şeker")


with open("newfile.txt","r+",encoding="utf-8") as file:
    print(file.read())

#sayfa başında güncelleme


with open("newfile.txt","r+",encoding="utf-8") as file:
    content=file.read()
    content ="efe tekir \n"+content
    file.seek(0)
    file.write(content)

print("*"*50)
with open("newfile.txt","r+",encoding="utf-8") as file:
    print(file.read())


#*******************************sayfanın ortasında güncelleme***********************************



with open("newfile.txt","r+",encoding="utf-8") as file:
    content= file.readlines()
    content.insert(2,"yılmaz aygün\n")
    file.seek(0)
    # for i in content:
    #     file.write(i)
    #burda for düngüsün yaptıgı isi daha koaly bir sekilde halletmemizi saglar
    file.writelines(content)
print("***"*50)

with open("newfile.txt","r+",encoding="utf-8") as file:
    print(file.read())


