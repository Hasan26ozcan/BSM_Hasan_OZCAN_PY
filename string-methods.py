message =" Hello There. My name is Sadık Turan "
print(message)# buda cümlenin direkt kendisi
message=message.upper()# bütün harfleri büyük yapıyor
print(message)
message=message.lower()# bütün hafleri küçük yapıyor
print(message)
message=message.title()#her kelimenin başını büyük yapıyor
print(message)
message=message.capitalize()#sadece ilk harf büyük oldu gerisi küçük oldu
print(message)
message=message.strip()# burda tam olarka yaptığı şey baştaki boşluğu sildiği
print(message)
##burdan sonrakiler ise dizi dediğimiz mantıkla meydana gelmektedir
message=message.split()#split metodu boşluğa kadar görür ve ordan bölerek yapar eğer içine
##bir değer girersek o şey görene kadar bölmez o şeyi görünce böler ve tekrar o şeyi 
#görünceye kadar bölmemeye devam eder
print(message)
print(message[0])
print(message[1])
message=" ".join(message)
print(message)

print(message.find("sadik"))
## bu metot aradığımız kelimenin ilk harfinin cümle içerisinde kaçıncı indekste
#olduğunuzu bulmamızı sağlar
# eğer aradığımız değer bu cümlede yok ise o zaman -1 değerini geri döndürür
print(message.startswith("h"))#h kelimesiylemi başlıyor
print(message.endswith("aan"))# n harfiylemi bitiyor

message=message.replace("m","My")
print(message)
message=message.replace("My","m")
print(message)
message=message.replace(" "," ")
print(message)
#bu replacede mesela makalelerde kullanabiliriz: 
message=message.replace("ç","c").replace("ö","o")#böyle devam edebilir
message=message.center(50,"*")
print(message)
print(len(message))








