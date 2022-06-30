#error handling

from logging import exception


try :
    x=int(input("x: "))
    y=int(input("y: "))
    print(x/y)    
except ZeroDivisionError as e:
    print("ikinci sayı için 0 değeri girilemez")
    print(e)#hatanın neyden olduğunu bize söylüyor
except ValueError as e:
    print("sayi harici farklı karakter girilemez")
    print(e)# hatanın ne odluğunu bize söylüyor
while True:
    try :
        w=int(input("w: "))
        z=int(input("z: "))
        print(w/z)    
    except Exception as e :#hatanın türü önemli degil hata gelmesi yeterli
        print(f"hatalı bilgi girdiniz: hatanız: {e} ")
    else : # unutmayalım exxcept ve else if else gibi biri çalışmazsa biri çalışır
        break
    finally:
        print("try metodu bitmiştir")



