#bankamatik uygulaması yapalım
a ={
    "ad":"hasan özcan",
    "hesapno": "123123123123",
    "bakiye":2000,
    "ekhasapbakiye": 1500
}
b ={
    "ad":"Mehmet Turan",
    "hesapno": "1234567890",
    "bakiye":3000,
    "ekhasapbakiye": 5000
}
print(a["bakiye"])

def paracek(hesapismi,miktar):
    print(f"merhaba {hesapismi['ad']} ")
    para= hesapismi["bakiye"]
    if(miktar<=para):
        hesapismi["bakiye"]= para-miktar
        print("para çekme işleminiz başarıyla gerçekleşmiştir")
        bakiyesorgula(a)
    elif(miktar>para):
        para1,para2=hesapismi["bakiye"],hesapismi["ekhasapbakiye"]
        paras= para1+para2
        if(paras>=miktar):
            print("bakiyeniz yetiyor ama ek hesaptanda para çekilmesi gerekiyor onaylıyormusunuz:\nonaylıyorum 1:|onaylamıyorum: 2")
            sayi=int(input())
            if(sayi ==1):
                paras= paras-miktar
                hesapismi["bakiye"]=0
                hesapismi["ekhasapbakiye"]=paras
                bakiyesorgula(a)
            elif(sayi==2):
                print("işleminiz bitmiştir")
            else:
                print("geçersiz işlem yaptınız:")
        else:
            print("paranız yetmiyor")
            bakiyesorgula(a)
    print("son durumda hesap bilgileriniz:")
    print(hesapismi)
def bakiyesorgula(hesap):
    print(f"{hesap['hesapno']} nolu hesabınızda hesap bakiyeniz  {hesap['bakiye']} TL bulunmaktadır ek hesap limitiniz ise {hesap['ekhasapbakiye']} ")


hesapadı=input("hesap adınızı giriniz: ")
paradegeri=int(input("para çekmek istediğiniz değeri giriniz: "))
paracek(a,1000)
bakiyesorgula(a)
print("**********************")
paracek(a,2000)
print("*************************")
paracek(a,500)
print("**************************")


