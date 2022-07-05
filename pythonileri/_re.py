import re
from turtle import st

print(dir(re))

#regular expression
# re modülü

str="python kursu: python all alll programlama kursu |999 40 saat pynbon"

print("**"*50)
coun=re.findall("python",str) # couunter
print(len(coun))
print(coun)

coun=re.split(" ",str)  #split
print(coun)

coun=re.sub(" ","-",str) #replace 
print(coun)

coun=re.search("python",str)
#0 ve 6 arasında oldugunu söylüyor
print(coun)
print(coun.span()) # aradıgımız degerin deger aralıgı
print(coun.start()) # aradıgımız degerin baslangıc noktası
print(coun.end()) #aradıgımız degerin bitis noktası
print(coun.group()) #aradığımız deger
print(coun.string) #aradıgımız degeri nerede arıyoruz
liste="[abcd]"
result=re.findall(liste,str)
print(result)
result=re.findall("[a-e]",str)
print(result)
result=re.findall("[saat]",str)
print(result)
result=re.findall("[a-z]",str)
print(result)
result=re.findall("[a-z]",str)
print(result)

# ama eğer [0-39] dersek burda  0 1 2 3 ve 9 olur 1 dan 39 a kadar gitmez
#[0-39] => [0 1 2 3 9]
 
result=re.findall("[^a-z]",str) 
# burada yapılmış olan işlemimizde ise onların haricindeki şeyleri alıyor
print(result)

result=re.findall("......",str)
print(result)

con=re.findall("py..on",str)
#burada ise ortasındaki degerler pek önemli değil ama yazılanları içermeli ve bu kadar haneye bölünerek yazılır
print(con)




#eger onunlamı başlıyor diye aratmka istersek eger ^a=şeklinde verilen ifadelerle yapabiliriz
#ama eğer bunlar hariç yada bu aralıkta demek istiyorsak o zaman [] parantez iine alarak yapmalıyız

result=re.findall("^python",str)
print(result)

#$ dolar işareti ise bununla bitiyormu diye kontrol ediyor bu işleve yarıyor

result=re.findall("n$",str)
result=re.findall("pynbon$",str)

print(result)

# hiç olmasada olur 1 tane de olsa olur çok fazla olsada olur ama farklı olamaz   "*"
result=re.findall("sa*t",str)
print(result)

# en az bir tane olmak zorunda çok fazla olabilir ama farklı olamaz  "+"
result=re.findall("py+thon",str)
print(result)
result=re.findall("p+thon",str)
print(result)
result=re.findall("sa+t",str)
print(result)

#en az sıfır en fazla 1 tane olabilir "?"
result=re.findall("p?thon",str)
print(result)


result=re.findall("al{2,3}",str)#al sayısında a dan sonra gelen l nin en az 2 en fazla 3 oldugu 
print(result)


result=re.findall("a{2}",str) # uzunluğu 2 olan a sayılarını getitir
print(result)


result=re.findall("[0-8]{2,3}",str)# en az iki en fazla da 3 basamaklı olan sayılarıda bize getirir
print(result)

result=re.findall("py|b",str)
print(result)



result=re.findall("(a|b|c)",str) # bu gruplama işlemi
print(result)

#\ özel isaretlerde aramızı saglar

result=re.findall("\Apython",str)
print(result)

result=re.findall("pynbon\Z",str)
print(result)


result=re.findall("\bon",str)#kelimenin başında mı
print(result)


result=re.findall("on\b",str)#kelimenin sonunda mı
print(result)


result=re.findall("\Bon",str)#kelime başında değilmi
print(result)


result=re.findall("on\B",str)# kelime sonunda değilmi
print(result)




result=re.findall("\d",str)#[0-9] ile aynı mantıkta sadece rakamları bize getiriyor
print(result)


result=re.findall("\D",str)#[^0-9] ile aynı mantıkda bu aralıkta olmayanları yani harfleri bize getiriyor
print(result)














