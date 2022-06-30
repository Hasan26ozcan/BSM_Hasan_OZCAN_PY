
x =10

# if x>5 :
#     raise Exception("x 5 ten üyüktür")

def checkpassword(psw):
    import re
    if (len(psw)<8):
        raise Exception("en az 8 karakter olmalıdır")
    elif not re.search("[a-z]",psw):
        print("hiç küçük harf içermemektedir")
    elif not re.search("[A-Z]",psw):
        print("bir büyük harf içermelidir")
    elif not re.search("[0-9]",psw):
        print("bir rakam içermelidir")
    elif not re.search("[_./@]",psw):
        print("bunlardan bir tanesini alpha  olmalıdır")
    elif re.search("\s",psw):
        print("parola bosluk icermemelidir")
    else: 
        print("geçerli parola")

psw=input("şifrenizi giriniz: ")

try:
    checkpassword(psw)
except Exception as a :
    print("islemde hatamız vardır",a)
else:
    print("islem basarili else kısmındaki bu")
finally:
    print("validation tamamlandı")


class person:
    def __init__(self,name,year):
        if(len(name)>10): # bu sayede istedigimiz alana istedigimiz sey olmasını saglıyor
            raise Exception("name alanı fazla karakter içeriyor")
        else:
            self.name=name
        if not(year>1900):
            raise Exception("yılınızı yanlış girdiniz:")
        else:
            self.year=year



p=person("ahmet",1890)

