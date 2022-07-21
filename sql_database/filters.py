from this import d
import mysql.connector 

def getprtodutcnyıd(ıd):
    connect=mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )
    cursor=connect.cursor()
    sql="SELECT * FROM `node-app`.produtcs where id=%s"
    params=(ıd,)# unumayalım burda onun sonrasında buraya "," koymamız gerekiyor
    cursor.execute(sql,params)
    # eger where yazıp ıd 1 dersek eger
    #ıd numarası 1 olan degerleri bize geri donduruyor eger name degeri verirsekte ona göre bir sorgulama
    #ve o name degerine ait bütün satırları getirir
    # eger içerisinde bir yazı birşey aramak istiyorsak eger o zaman kullanmamız gerekn şey
    # cursor.execute("SELECT * FROM `node-app`.produtcs where name LIKE '%iphone%' ")
    # eger burda % işaretinden ilkini kaldırırsak eger iphone ile başlayanlar 
    # arkadaki yüzde işaretini kaldırırsak eger iphone ile bitenleri bize getiriyor
    result=cursor.fetchall()# fetchall ile fetcone arasındaki fark
    # birisi hepsini getirir ötekisi ise koşulu sağlayan ilk kaydı getirmesini saglıyor
    # fetchall liste halinde geri döndürür ama one liste halinde degil tek deger halinde geri döndürür
    print(result)
    for i in result :
        print(f"id {i[0]} name: {i[1]} price: {i[2]} ")



getprtodutcnyıd(11)











