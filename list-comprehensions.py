from tkinter import Y


numbe =[]
for x in range(10):
    numbe.append(x)
print(numbe)
numbers=[x for x in range(10)]
print(numbers)
print("**"*50)

for x in range(10):
    print(x**2)
print("//"*50)
numbers =[x**2 for x in range(10)]
print(numbers)
print("//"*60)

numbers =[x**2  for x in range(3,12,2) if x%3 ==0 ]
print(numbers)


mystring ="Hello"
mylist= []

for x in mystring:
    mylist.append(x)
print(mylist)

mylist=[x for x in mystring]
print(mylist)



years =[1983,1999,2008,1956,1986]
ages = [2022-x for x in years ]

print(ages)

result=[]
result =[f"çift sayi : {x}" if x%2==0   else f"tek sayi : {x} "  for x in range(1,10)]
print(result)

for sayi in result:
    print(sayi) 



result =[]


for a in range(3):
    for b in range(3):
        result.append((a,b))

print(result)
print(result[1][1])


numbers =[]
numbers =[(x,y,z) for x in range(3)  for y in range(3) for z in range(3)]
print(numbers)