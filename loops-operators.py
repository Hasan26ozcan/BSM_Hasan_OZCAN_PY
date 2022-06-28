liste =[1,2,3]

for item in range(9,100,11):
    print(item)
lit=[]
print(list(range(9,100,11)))

greeting ="Hello World"
index=0
for letters in greeting:
    print(f"index değer : {index}   letters değeri {letters} ")
    index+=1
print("**"*50  )

for items in enumerate(greeting):
    print(f" itemleri : {items} ")
print("**"*50)

for index,letters in enumerate(greeting):
    print(f"indeks {index}  letters: {letters} ")
print("**"*50)
#zip dosyası


list1=[1,2,3,4,5]
list2=["a","b","c","d","e"]
list3=[100,200,300,400,500]


print(list(zip(list1,list2,list3)))


for item in zip(list1,list2,list3):
    print(item)
