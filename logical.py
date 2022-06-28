x =5
hak ="e"
result = 5<x<10
print(result)
#and
result= ((x>5) and (x<10))
result= (x>5) and (hak =="e")
print(result)
#or
resulta= (x >0) or (x<0)

print(resulta)
#not
x =4
# burda eğer kıoşul doğru ise not onu tam tersi yaparak yanlış yapıyor yani
resultsa=(not(x>0))
print(resultsa)

# x, 5-10 arasında olan bir çift sayı mı
result =((x>5) or (x<10)) and (x%2==0)
print(result)



