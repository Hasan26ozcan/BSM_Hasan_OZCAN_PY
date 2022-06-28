def changename(n):
    n="ada"

name="yiğit"
changename(name)
print(name)
liste=["ankara","eskişehir","bursa","ankara"]
print(liste)
def change(n):
    n[0]="istanbul"
change(liste)
print(liste)

n=liste
n[0]="safari"
print(n)
print(liste)

n=liste[:]#bu işlemde aynısından n de bir tane daha oluşturuyoruz onun referansını ona vermemiş oluyoruz
n[0]="hakkari"
print(n)
print(liste)

def add(a,b,c=0):
    return sum((sum((a,b,c)),sum((a,b,c))))# sum bizden bir fonksiyon bekliyor bu yüzden birde ayrıyetten bir tane daha paranteze alıyoruz
# burda kullandığımız şey istersek bazen 2 bazen 3 parametreli birşekilde kullanmamızı sağlıyor bu kodda devamlılık için güzel


print(add(10,30))
print(add(12,45,78))
sum=0
def adds(*params):# burda ise biz bi sınırlandırma koymuyoruz ve istediği kadar değer girip toplama işlemini yerine getiriyor
    print(type(params))# buraki tek yıldız ise liste göndermek istiyorsak tuple listesi göndermek istiyorsak
    print(params) #tuples oalrak ekrana yazdırılıyor
    sum=0
    for n in params:
        sum +=n
    return sum


print(adds(12,56,96,52,41,73,59,85))

def displayuser(**paramets):#iki yıldızın gelmesindeki amaç dictionary geliceğini haber vermektir
    print(type(paramets))
    for key in paramets:
        print(f" {key} is {paramets[key]} ")

        




displayuser(name="çınar",age=2,city="istanbul")
displayuser(name="ada",age=12,city="kocaeli",phone=12345678)
displayuser(name="yiğit",age=123,city="ankara",phone=12345678,email="yigit@email.com")


def mymunch(a,b,*list,**kwargs,):
    print(a)
    print(b)
    print(list)
    print(kwargs)


mymunch(2,"samet","ahmet","mehmet","funda","mehmet",name = "çınar",age = 12, sadi ="para")



