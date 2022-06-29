class person:
    adress = "bilgi yok"

    def __init__(this,name,birthyears):
        this.name=name
        this.birthyears=birthyears
#burda ise normal bir metot yapıyorum
    def intro(this):
        print(f"hello {this.name} ")

    def yearsold(this):
        return 2022-this.birthyears

p1=person("ahmet",2003)
p2=person("ali",1999)

p1.intro()
p2.intro()

print(p1.yearsold())
print(p2.yearsold())


class Circcle:
    #class object attribute
    pi=3.14

    def __init__(self,yarıcap=1):#bu işlemde eğer yarıçap belirtilmediyse ona 1 değeri atmamızı sağllıyor
        self.yarıcap=yarıcap

    def alan(self):
        return  self.pi*(self.yarıcap**2)

    def çevresi(self):
        return 2*self.yarıcap*self.pi

sayi1=int(input("yarıçap degerinizi giriniz: "))

p1=Circcle(sayi1)
print(p1.alan())
print(p1.çevresi())

