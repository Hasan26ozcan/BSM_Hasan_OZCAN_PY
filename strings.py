name ="Sadık"
surname='Turan'
age =36
greeting="My name is: "+name+" "+surname+" and \nI am "+str(age)+" years old"
print(greeting)
# burada unutmayalım age str koymadan yaparsak da olur ama "," kullanmamız gerekir
#print("My name is: "+name+" "+surname+" and I am",age,"years old")
# onundeki bosluk ve arkasimdaki bosluk degerini sildim cunku age kendine göre bosluk koyuyor
length=len(greeting) # burda bize length greeting uzunluğunu veriyor



# print(name[4])
# print(length)
# print(type(length))
# print(greeting[len(greeting)-1])
# print(greeting[-1])
print(greeting[3:5])# burda 3 4 indeklerindeki elemanı al
print(greeting[15:]) # burada ise 15. indeksten sonuna kadarkileri al
print(greeting[:15]) # burda ise başından 0 indeksten 15. indekse kadar al

print(greeting[2:40:4]) # 2 den 40. karaktere kadar gir ama 4 karakterde 1 al 


# ve diğer birsey ise buda oluyor onun uzunlugunun 1 eksigi olması gerektigini biliyoruz
#ama eger direkt olarak -1 yazarsak gene son elemanını alıyor ve -2 yazarsak ise sondan 
# bir önceki elemanını alıyor yani - taraf sondan basa geliyor