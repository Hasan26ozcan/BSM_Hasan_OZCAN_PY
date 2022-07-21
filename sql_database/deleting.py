import mysql.connector
def prodatcs():
    connector=mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
    )
    cursor=connector.cursor()
    sql="select * FROM `node-app`.`produtcs` "
    cursor.execute(sql)
    result=cursor.fetchall()
    for i in result:
        print(i)


def deleteid(id):
    connector=mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
    )

    cursor=connector.cursor()
    sql="DELETE FROM `node-app`.`produtcs` WHERE (`id` = %s)"
    values=(id,)
    cursor.execute(sql,values)

    try:
        connector.commit()
        print(f"{cursor.rowcount} tane kayır silinmiştir")
    except Exception as err:
        print("hata",err)
    finally:
        connector.close()
        print("işleminiz başarıyla gerçekleştirilmiştir")

deleteid(12)
prodatcs()