"""
    ogrenciler ={
        "120":{
            "ad": "Ali",
            "soyad":"yılmaz",
            "telefon": "532 000 00 01
        },
        "125" : {
            "ad" :"can",
            "soyad" :"korkmaz",
            "telefon" :"532 000 00 02"
        },
        128 :{
            "ad" :"Volkan" ,
            "soyad" :"yükselen",
            "telefon": "0532 000 00 03"
        }
    }
1- bilgileri verilen  ogrencileri kullanicidan aldiginiz bilgilerle dictionary içinde
saklayiniz

2- ogrenci numarasını kullanicidan alip ilgili ogrenci bilgisi gosterin

"""

numbers= input("numaranızı giriniz: ")
name=input("ismini giriniz:")
surname=input("soy adını giriniz:")
numbers =numbers.strip()
telefonnumbers =input("telefon numarasını giriniz: ")
ogrenciler ={
        numbers:{
            "ad": name,
            "soyad": surname,
            "telefon" : telefonnumbers

        }
    }
numbers= input("numaranızı giriniz: ")
name=input("ismini giriniz:")
surname=input("soy adını giriniz:")
numbers =numbers.strip()
telefonnumbers =input("telefon numarasını giriniz: ")
ogrenciler.update({
    numbers :{
        "ad":name,
        "soyad":surname,
        "telefon":telefonnumbers
    }
})
numbers= input("numaranızı giriniz: ")
name=input("ismini giriniz:")
surname=input("soy adını giriniz:")
numbers =numbers.strip()
telefonnumbers =input("telefon numarasını giriniz: ")
ogrenciler.update({
    numbers :{
        "ad":name,
        "soyad":surname,
        "telefon":telefonnumbers
    }
})
print(ogrenciler)
print("*"*50)

# "}" parantez ve ")" arasına "," koyarak devam ettirtebiliriz
    #eğer olan bir sayıyı girersek işte o zaman onun üstüne yazma işlemini yerine getiriyor
number= input("ogrenci numarasını giriniz: ")
ogrenci=ogrenciler[number]
print(ogrenci["ad"])
print("ogrenci adi: {} \nogrenci soyadı: {} \nogrenci telefon numarası: {}".format(ogrenci["ad"],ogrenci["soyad"],ogrenci["telefon"]))
print(f"ahmet {ogrenciler[number]} ")


