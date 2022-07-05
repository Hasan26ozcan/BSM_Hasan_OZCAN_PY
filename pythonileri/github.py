
import requests
import json
#api kullanmanın önemi burda anlıyoruz
class Github:
    def __init__(self):
        self.__api__="https://api.github.com"
        self.token="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"
        #token olan yere kendi token bilgimizideki sayıları koyuyoruz tokende sayılar için 
    def getuser(self,username):
        rest=requests.get(f"{self.__api__}/users/{username}")
        jsons=json.loads(rest.text)
        return jsons
    def getreposityname(self,username):
        rest=requests.get(f"{self.__api__}/users/{username}/repos")
        respo=json.loads(rest.text)
        return respo
    def creativereposity(self,name):
        response = requests.post(f"{self.__api__}/user/repos?access_token={self.token}",json={
            "name":name,
            "description":"This is your first reposiity",
            "homepage":"https://github.com",
            "private":False,
            "has_issues":True,
            "has_projects":True,
            "has_wiki":True
        })
        return response.json()

github=Github()


while(True):
    secim=input("1- Find user\n2- Get reposity\n3- Create reposity\n4- Exit")
    if(secim=="4"):
        break
    else:
        if(secim=="1"):
            username=input("username bilginizi giriniz: ")
            resulta=github.getuser(username=username)
            print(f"name: {resulta['name']} result:  {resulta['public_repos']} follewers: {resulta['followers']}  ") 

        elif(secim=="2"):
            username=input("username bilginizi giriniz: ")
            rest=github.getreposityname(username=username)
            for i in rest:
                print(i["name"])


            
        elif(secim=="3"):
            name=input("repository name")
            resultas=github.creativereposity(name)
            print(resultas)

