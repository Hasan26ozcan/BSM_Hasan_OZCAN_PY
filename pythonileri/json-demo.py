import json
import os
class User:
    def __init__(self,username,passwords,email) :
        self.username=username
        self.password=passwords
        self.email=email


class UserRepository:
    def __init__(self):
        self.users=[]#burda dosyadaki herşeyi alıyoruz okuma işlemi falan olursa buradan halledicez
        self.islogged=False # burada ise yaptıgımız islem ise eger sisde giris olduysa bunu True yapıyoruz
        self.currentuser= {} # burada ise yaptıgımız seyde eger giris basarılı ise onun bilgileri burada tutulucak
       # self.loadUser()
    

# unutmayalım loads sayesinde jsondan dışarı çıkmamızı sağlıyoruz ve bu sayede değerlere daha kolay eişmemizi sağlıyoruz
#ama eğer jsona ekleme yapıcaksak eger o zaman dumps metodunu kullanarak ekleme işlemini yerine getiriyoruz
    def loadUser(self):
        if(os.path.exists("users.json")):
            with open("users.json","r",encoding="utf-8") as find:
                user=json.load(find)
                print(user)
                for a in user:
                    user=json.loads(a)
                    newuser=User(username=user["username"],passwords=user["password"],email=user["email"])
                    self.users.append(newuser)
        print(self.users)

    def register(self,User:User):
        self.users.append(User)
        self.savetofile()
        print("kullanıcı oluşturuldu")

    def login(self,username,password):
        for a in self.users:
            if a.username==username and a.password==password:
                self.islogged=True
                self.currentuser=username
                print("login yapıldı")

    def savetofile(self):

        list=[]

        for user in self.users:
            list.append(json.dumps(user.__dict__))




        with open("users.json","w",encoding="utf-8") as file:
            add=json.dumps(list)# dump o hale getirip kayıt etme işleminde kullanılır ama dumps da ise json kayıt haline getirilir
            #ama kayır edilmez
            file.write(add)
        



reporsity= UserRepository()
reporsity.loadUser()

while(True):
    print("Menu".center(50,"*"))
    a= int(input("1-Register\n2- Login\n3- Logout\n4- identity\n5- Exit\ncevabınız: "))
    if(a==1):#register
        username=input("username bilinizi giriniz: ")
        password=input("pasword bilinizi giriniz: ")
        email=input("email bilinizi giriniz: ")
        user=User(username=username,passwords=password,email=email)
        reporsity.register(user)


        print(reporsity.users)
        pass
    elif(a==2):#login
        if(reporsity.islogged==True):
            print("zaten sistemde birisi var")
        else: 
            username=input("kullanıcı adınızı giriniz: ")
            password=input("şifrenizi giriniz: ")
            reporsity.login(username=username,password=password)
    elif(a==3):#logout
        reporsity.islogged=False
        reporsity.currentuser={}
        print("çıkış yapıldı")
    elif(a==4):#display username
        if(reporsity.islogged==True):
            print(reporsity.currentuser)
        else:
            print("sisteme giriş yapılmamıştır")
    elif(a==5):#exit
        break
    else:
        print("yanlış işlem yapıldı")
        break







