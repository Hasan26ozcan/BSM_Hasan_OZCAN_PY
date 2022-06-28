number =[1,2,3,4,5]
num=0
while num <len(number):
    print(number[num])
    num+=1
print("//"*50)    
print(num)
print("//"*50)
#1 den 100 e kadar bütün sayıları ekrana yazdırınız: 
numb=1
while(numb<=100):
    if(numb % 2 ==0):
        print(f"çift sayi : {numb}  ")
    else:
        print(f"tek sayı :  {numb}  ")

    numb+=1
print("bitti...")
#kullanıcıdan değer isteyelim 

name ="" #False 
# String bir değer boş olarak yaptığımızda yanlış olarak sayıyor

while not name:
    name =input("isminizi giriiniz: ")
    name =name.strip()
print(name)
