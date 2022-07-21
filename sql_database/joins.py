import mysql.connector

def getprtodutcs():
    connect=mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )
    cursor=connect.cursor()
   # cursor.execute("SELECT * FROM `node-app`.products inner join categories on categories.id=products.categoryid ")
    #cursor.execute("SELECT products.name,products.price,categories.name FROM `node-app`.products inner join categories on categories.id=products.categoryid")
    cursor.execute("SELECT products.name,products.price,categories.name FROM `node-app`.products inner join categories on categories.id=products.categoryid where categories.name='Telefon' ")

# burda ise ona o degerde karşılık gelenler geliyor
    try:
        result=cursor.fetchall()
        for i in result:
            print(i)
    except Exception as err:
        print("hata",err)
    finally:
        connect.close()


getprtodutcs()

