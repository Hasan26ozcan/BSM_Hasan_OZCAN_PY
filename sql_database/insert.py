import mysql.connector

# bu fonksiyonda tek tek ekleme işlemi yapabiliriz
def insertprodutcs(name,price,imageUrlId,description):
    connect=mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )
    cursor=connect.cursor()
    sql=("INSERT INTO `node-app`.`produtcs` (`name`, `price`, `imageUrld`, `description`) VALUES (%s,%s,%s, %s)")
    value=(name,price,imageUrlId,description)
    cursor.execute(sql,value)

    try:
        connect.commit()
        print(f" {cursor.rowcount} tane kayıt eklendi ")
        print(f" son kaydın ıd numarası {cursor.lastrowid} ")
    except Exception as error:
        print("hatalı işlem yaptınız",error)
    else:
        print("işleminiz başarılı bir şekilde gerçekleşmiştir")
    finally:
        connect.close()
        print("database bağlantısı kapandı")




# burda ise 1 den fazla sayıda eklemesini saglıyoruz
def insertprodutcs(liste):
    connect=mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )
    cursor=connect.cursor()
    sql=("INSERT INTO `node-app`.`produtcs` (`name`, `price`, `imageUrld`, `description`) VALUES (%s,%s,%s, %s)")
    value=liste
    cursor.executemany(sql,value)

    try:
        connect.commit()
        print(f" {cursor.rowcount} tane kayıt eklendi ")
        print(f" son kaydın ıd numarası {cursor.lastrowid} ")
    except Exception as error:
        print("hatalı işlem yaptınız",error)
    else:
        print("işleminiz başarılı bir şekilde gerçekleşmiştir")
    finally:
        connect.close()
        print("database bağlantısı kapandı")

liste2=[]
while True:
    name=input("adınızı giriniz: ")
    price=float(input("fiyatını giriniz: "))
    imageUrlId=input("forograf urlsini giriniz: ")
    description=input("nasıl oldugunu giriniz: ")
    devam=input("devam etmek istiyormusunuz (e/h)")
    liste2.append((name,price,imageUrlId,description))
    if(devam=="h"):
        print("eklenen listeler")
        print(liste2)
        insertprodutcs(liste2)
        break
    elif(devam=="e"):
        True

    else:
        print("geçersiz islme yaptınız")

    
 