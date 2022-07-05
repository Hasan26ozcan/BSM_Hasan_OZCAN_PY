# themoviedb.org => film ve dizi arşivi
# themoviedb' nin sunduğu apiyi uygulamanızda kullanın
# anahtar kelimelere doğru arama
# en popüler film
# vizyondaki fil listesi


import requests

class themoviedb:
    def __init__(self):
        self.api="https://api.themoviedb.org/3"
        self.api_key="df7531dea460bd08072d12e822120599"

    def gepopulatire(self):
        responsiypolatire=requests.get(f"{self.api}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return responsiypolatire.json()
    def search(self,write):
        searchmoviekey=requests.get(f"{self.api}/search/keyword?api_key={self.api_key}&query={write}&page=1")
        return searchmoviekey.json()


themovie=themoviedb()

while(True):
    seçim=input("1- popularite\n2- kelimeye göre siralama\n3- Exit")
    if(seçim=="3"):
        break
    else:
        if(seçim=="1"):
            result=themovie.gepopulatire()
            for i in result["results"]:
                print(i["title"])
        elif(seçim=="2"):
            degeriniz=input("aramak istediginiz kelimeyi giriniz: ")
            lsitesi=themovie.search(degeriniz)
            print(lsitesi)
            for i  in lsitesi["results"]:
                print(i["name"])




