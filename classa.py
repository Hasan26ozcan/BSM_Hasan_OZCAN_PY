#class

#class person:
#    attribuat

#bu klasda attribuat ve methodlari icerisine yazabiliriz
#          oznitelikler  ve metotlar

#    metot

#eger burda 
class persons:
    pass
    adress ="no information"
    # class attribuar 
    # bu islemleri yapmak icin yapılandırıcıları kullanırız

    def __init__(self,name,year):
        self.name=name
        self.year=year
        print("init metodu çalışıyor")
        # burda illa self yazmak zorunda degiliz onun yerine this de yazabiliriz
        



    # object attribuar

    #methods




#unutmayalim sadece 1 tane class tanimlayabiliriz bir yerde ve eger icerisine pass yazarsak bize bir hata dondurmez


#attributes bizim int string degerimiz gibi oldugumu için onu public oldugu surece erisme konusundan boyle yapılıyor
# yani attributes bizim uzantımız gibi dusunebiliriz 


#object, instance

#acsessing object attributes
p1=persons("hasan",2020) #burada yaptigimiz islem ise persons classindan bir obje uretme islemi gerceklestirdi
p2=persons(name= "mehmet",year=1978) # boyle yaptıgımızda ise okunabilirligini arttırmıs oluyoruz
p1.name="Ali"
p1.adress="kocaeli"
print(f"p1 için {p1.name} {p1.year} {p1.adress} ")
print(f"p2 için {p2.name} {p2.year} {p2.adress} ")
print(type(p1))
print(type(p2))
print(p1 == p2) # burda tam olarak onların adreslerini karşılaştırıyor 



