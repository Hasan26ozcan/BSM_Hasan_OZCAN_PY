import random
from telnetlib import PRAGMA_HEARTBEAT

print(dir(random))

print(random.random()*100) #burda bize 0 ve 1 arasında bir sayi uretmemizi saglıyor ve hemen arkasindan 
#100 ile carptigimizda o sayının 2 virgül t-yanına atarak bize kolaylik sagliyor
print(random.randint(0,9))

print(random.uniform(1.5,2.1))

gretting="Hello there"
names=["Ali","Mehmet","Veli","Yağmur","Deniz","Cenk"]
print(names[random.randint(0,len(names)-1)])

print(random.choice(names))
#bu metot ise ise bize burda erdiğimiz dizide random birini döndürüyor üstekinin kisa yolu

print(random.choice(gretting))

liste=list(range(0,10))
print(liste)
random.shuffle(liste)
print(liste)
liste.sort()
print(liste)

liste=list(range(0,101))
print(liste)

print(random.sample(liste,4))

