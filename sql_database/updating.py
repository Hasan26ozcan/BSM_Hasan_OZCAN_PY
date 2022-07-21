import mysql.connector
def updateprodutc(id,name,price):
    connect=mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="schooldb"
    )
    cursor=connect.cursor()
    sql="UPDATE `node-app`.`produtcs` SET `name`=%s,price=%s,description='güzel telefon' WHERE (`id` = %s)"
    values=(name,price,id,)
    cursor.execute(sql,values)
    try:
        connect.commit()
        print(f" {cursor.rowcount} tane kayıt güncellenmiştir ")
    except Exception as err:
        print(f"HATA  {err} ")
    finally:
        connect.close()
        print("işlem başarılı bir şekilde yapılmıştır")

updateprodutc(1,"i20",400)

