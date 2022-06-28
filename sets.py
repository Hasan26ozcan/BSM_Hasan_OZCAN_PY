fruits1={"apple","banana","orange"}
fruits2=["apple","banana","orange"]
print(fruits2[0])
#print(fruits1[0]) bu değer indekslenemez indekslenemeyen bir listede

for x in fruits1:{
    print(x)
}
print("*"*100)
addet={"ahmet",123,123123123,"apple","banana","banana","banana","banana","banana"}
#setlerin bir diğer özelliği bir kelimeden sadece bir tane tutuyorlar
fruits1.add("cherry")
fruits1.update(addet)
for x in fruits1:{
    print(x)
}
print(fruits1)
fruits1.remove("banana")
fruits1.discard("")
print(fruits1)
fruits1.pop()
print(fruits1)
print("*"*50)
fruits1.clear()
print(fruits1)
mylist=[1,2,5,4,4,2,1]
print(mylist)
print(set(mylist))
print(mylist)



