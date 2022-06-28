"""
Soru: Girilen bir sayının asal olup olmadığını bulun.
** Asal sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir
"""

sayi1=int(input("sayınızı giriniz: "))
counter=1
coun=0
while(counter<=sayi1 ):
    if(sayi1%counter==0):
      coun+=1 
    counter+=1 
if(coun ==2):
    print(f" {sayi1} bu sayi asal bir sayıdır ")
else:
    print(f" {sayi1} bu sayı asal bir sayı değildir ")
sayi1 =int(input("sayı giriniz: "))
counter=0
for x in range(1,sayi1+1):
    if(sayi1%x ==0):
        counter+=1
if(counter == 2):
    print("bu sayı bir asal sayıdır")
else :
    print("bu sayı asla bir sayı değildir")

asalmi =True

for c in range(2,sayi1):
    if(sayi1%c==0):
        asalmi=False

if asalmi:
    print("sayımız asal sayıdır")
else:
    print("sayımız asla bir sayı değildir")

