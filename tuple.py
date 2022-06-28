from this import d


list =[1,2,3]

tuple=(1,"iki", 3)

print(type(list))
print(type(tuple))

print(list[2])
print(tuple[1])

list= ["ali","ahmet"]
tuple=("damla","ayşe","ayşe")
names=("demet","fatma","emel")+tuple# burda sadece tuple ile tuple toplanıyor
list1=["123","123123"] +list# burdada olduğu gibi sadece listler toplanıyor
#listler ve tuple lar birleştirilemiyor
print(list1)

#listelerle tuple aynı işlevi yapıyorlar sadece listte bir elemana birşey atayabiliyorken
#tuple bir elemana birşey yazdıktan sonra o elemana birşey atayamıyoruz
#list. bize kullanabileceğimiz çok şey var olduğunu gösteriyor
#tuple.  ama tuple da lsite kadar çok fazla şey yok
print(list)
print(tuple)
print(names)


#str="asdasdasd"
#print(str.rindex("d"))
# bu kısım ise sağdan bulmak istersek diye ama unutmayalım bu stringlerde işey yarıyor


print(tuple.index("ayşe"))

