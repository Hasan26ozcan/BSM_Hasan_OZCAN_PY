def square(num): return num**2
result=square(2)
print(result)
numbers =[1,2,3,4,5,6]
resulta=list(map(lambda num:num**3 ,numbers))
# numbersin içerisindeki değerleri tek tek square fonksiyonuna gönderim return ediyor
print(resulta)
liste=[]
for x in map(square,numbers):
    liste.append(x)
print(liste)

print(list(map(lambda num:num**2  ,(5,6))))
#lambda expressions dediğimiz şey ise bizim o metoda ihtiyacımız yok onu daha kısa sürede yapmamızı sağlıyor

sqkiz=lambda num: num**2 
result=list(map(sqkiz,(5,6,7)))
print(result)

# listes=[z if z%3==0 else ""  for z in range(1,40) if(z%2==0)]
# result =[f"çift sayi : {x}" if x%2==0   else f"tek sayi : {x} "  for x in range(1,10)]
# print(listes)

screan= sqkiz(4)
print(screan)
def check_even(num):
    return num%2==0


lis=list(filter(lambda num:num%3==0,(3,4,5,9)))
print(lis)



ceheck_iven_my=lambda num:num%3
numbers=[x for x in range(1,101)]
mylist=list(filter(ceheck_iven_my,numbers))
print(mylist)

result=ceheck_iven_my(numbers[2])# burdaki saynın o işlemi sağlayıp sağlamadığıan bakabiliriz bu sayede
print(ceheck_iven_my(numbers[2]))

print(result)