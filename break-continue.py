from operator import le


name ="Sadik Turan"

for letters in name:
    if(letters == "a" ): #burda ise a harfini gördüğü zaman direktmen döngyü bitirir
        break
    print(letters)

for letters in name: # burda a harfini ekrana yazdırmaz onu atlar ve geriye kalanları ekrana yazdırır
    if(letters == "a" ):
        continue
    print(letters)

x =0

while ( x < 5 ):
    if (x == 2):
        x+=1
        continue
    print(x)
    x+=1


#1 - 100 e kadar tek sayıların toplamı

 
toplam=0
x=1
while(x<100):
    if(x %2 ==0): 
         x+=1
         continue
    print(x)
    toplam+=x
    x+=1
   
    

print(toplam)

toplam=0
x=0
while( x<100):
    if(x%2 ==0):
        toplam+=x
    x+=1    

print(toplam)

toplam=0
counter =0
while(counter<=100):
    toplam+=counter
    counter+=1
print(toplam)

toplam=0
for x in range(1,101):
    toplam+=x
print(toplam)