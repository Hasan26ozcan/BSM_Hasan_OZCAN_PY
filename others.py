#Identyity Operator: is

x = y= [1,2,3]
z=[1,2,3]
# is yaptığımzıda
# onların referanslarını karşılaştırıyoruz  
print(x == y)
print(x == z)
print(x is y)
print(x is z)

x =[2,1,3]
print(x == y)
print(x is y)
del x[2]
print(x)
y =[2,4]
print(x == y)
print(x is y)
y[1]=1
print(y)
print(x == y) # elemanları eşittir operatorü karşılaştırdığımzıda doğru geliyor
print(x is y) # ama referansaları aynımı diye baktığımızda farklı
print(x is not y) # not objesiylede yaptığımız şeyi tersini alıyoruz onun refansımı değilmi gibi tersi



#Membership Operator: in
print("**"*50)
# in operatoru bu değer burada varmı içinde varmı diye kontrol etmemizi sağlıyor
x =["apple","banana","orange"]
print("apple" in x )

name ="Hasan"
print(name.count("a"))
print("f" not in name)


