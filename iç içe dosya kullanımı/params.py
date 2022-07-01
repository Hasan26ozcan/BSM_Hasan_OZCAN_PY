def toplama(a,b):
    return a+b
def çıkartma(a,b):
    return a-b
def çarpma(a,b):
    return a*b
def bölme(a,b):
    return a/b
#hazırlamış oldugumuz fonksiyonları başka fonksiyonların icerisine göndermemizi saglıyor
def islem (f1,f2,f3,f4,islem_adı):
    if(islem_adı=="toplama"):
        print(f1(2,4))
    elif(islem_adı=="çıkartma"):
        print(f2(5,7))
    elif(islem_adı=="çarpma"):
        print(f3(4,7))
    elif(islem_adı=="bölme"):
        print(f4(56,21))
    else:
        print("geçersiz islem yaptınız")

islem(toplama,çıkartma,çarpma,bölme,"toplama")
islem(toplama,çıkartma,çarpma,bölme,"çıkartma")
islem(toplama,çıkartma,çarpma,bölme,"çarpma")
islem(toplama,çıkartma,çarpma,bölme,"bölme")
