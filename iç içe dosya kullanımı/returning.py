# bir fonksiyondan bir fonksiyon gönderme islemine 


from nntplib import ArticleInfo


def uslama(number):

    def inner(power):
        return number ** power
    
    return(inner)


two= uslama(3) #burda iner referansını atmış oluyoruz
sayi= two(5)
print(sayi)

def yetki_sorgula(page):
    def inner(role):
        if("admin"==role):
            return(f"{role} rolü {page} sayfaya erişebilir ")
        else:
            return(f"{role} rolü {page} sayfaya erişemez ")
    return inner

sayfa=input("hangi sayfaya gitmek istersiniz:") 
page= yetki_sorgula(sayfa)
rolünüz=input("rolünüzü giriniz: ")
print(page(rolünüz))

def islem(islemadı):
    def toplama(*args):
        toplam=0
        for i in args:
            toplam=+toplam+i
        return toplam
    def çarpma(*args):
        carpma=1
        for i in args:
            carpma=carpma*i
        return carpma
    if islemadı=="toplama":
       return toplama
    elif islemadı=="çarpma":
        return  çarpma
 
sayi= islem("toplama")
print(sayi(1,2,3,4,5,6,7,8,9))

sayi=islem("çarpma")
print(sayi(1,2,3,4,6))




