def sayHello(name = "user"):
    print(f"Hello {name} ")

sayHello("Barışcan")
sayHello("Hasan")
sayHello("Metehan")
sayHello()# diyelimki, değer girmeyi unuttuk işte o zaman bizim yerimize şunu gird diye fonksiyonda tanımlıyoruz

def sayHellos(name= "user"):
    return f"Hello {name} " 

print(sayHellos("= Merhaba"))


def total(num1,num2):
    return num1+num2

print(total(10,20))
print(total(100,200))


def yashesapla(gününyili,dogumyili):
    return gününyili-dogumyili
print(yashesapla(2019,2003))


def emekliligenekadarkaldi(dogumyili,isim):
    """
    DOCSTRİNG: dogum yiliniza emeklilik durmunuzu ögrenmenizi sagliyor
    INTPUT : dogumyili
    OUTPUT : hesaplanan yil bilgisi
    """


    yas=yashesapla(2019,dogumyili)
    emeklilikicingerekenyas=65
    kacyilvar=emeklilikicingerekenyas-yas
    if(kacyilvar>0):
        return f" {isim} için gereken sene {kacyilvar} "    
    elif(kacyilvar==0):
        return "hayırlı olsun günleri sayabilirsiniz"
    else:
        return f"emekli olunmuştur hayırlı olsun emekli olunan yıl sayisi {-1*kacyilvar} "

print(emekliligenekadarkaldi(1953,"hakan"))

#eger yine kodu calistirirkensorun cikarsa diye help fonksiyonunu kullanabiliriz

print(help(emekliligenekadarkaldi))#emeklilige ne kadar kaldi icin nasil kullanmamiz gerektigi ne ise yaradigi hakkinda 
#bilgi almamızı sagliyor
print(help(list.append))
#burda ise append metodunun ne ise yaradğını bulmaya calisiyor

