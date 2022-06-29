mylist=[1,2,3]
mtStrigns="my string"


print(len(mylist))
print(len(mtStrigns))
print(type(mylist))
print(type(mtStrigns))

class movie:
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
        print("movie objesi başarılı bir şekilde oluşturulmuştur")
    def __str__(self):
        return f" {self.title},{self.director},{self.duration}"
    def __len__(self):
        return self.duration
    def __del__(self):
        print("movie silindi")






 
m=movie("film adı","yönetmen",120)
print(type(movie))
# print(len(movie))
print(m)

#aslında biz ekrana birşey yazdırmak istedigimizde arka tarafta calısan metodumuz bizim str metodudur

m.__str__()

print(len(mylist))
print(len(m))


#ama soyle birseyde var biz olusturduk ama belli bir sure kullanmadıysak o kendi kendine gene siliniyor



del m
## eger del metodu ile silme islemini yerine getiriyorsak sonra bu seyi bulamayabiliriz
# print(m)


