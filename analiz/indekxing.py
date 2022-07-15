import numpy as np

numberss=np.array([0,5,10,15,20,15,50,75,85])


results=numberss[1]
print(results)


results=numberss[1]
print(results)

results=numberss[-1]
print(results)

results=numberss[0:3]
print(results)

results=numberss[:5]
print(results)


results=numberss[1:]
print(results)

results=numberss[-7:-3]
print(results)

results=numberss[::-2]
print(results)

results=numberss[7:2:-1]
print(results)

print("***"*30)
numbeerrss=np.array([[0,5,10],[15,20,15],[50,75,85]])

print(numbeerrss)
print()
results= numbeerrss[0]
print(results)

results= numbeerrss[2]
print(results)

results= numbeerrss[0,2]
print(results)

results= numbeerrss[2,1]
print(results)

results= numbeerrss[:,1]# burda ise her sutunun 1. indeksini kullanarak onları ekleyerek bir liste oluşturulmasını saglıyor
print(results)

results= numbeerrss[:,0:2]# burda ise tüm elemanlarda 0 ve 2 arasındakileri bana getir
print(results)

results= numbeerrss[-1,:]
print(results)

results= numbeerrss[0:3,0:3]
print(results)

results= numbeerrss[0:2,0:2]
print(results)

# pylist=[[0,5,10],[15,20,15],[50,75,85]]
# print(pylist[0,0])
# bu python listesinde olmayan ama numpy listesinde olan farklı bir özelliktir




arr1=np.arange(0,10)
arr2=arr1
arr3=arr1.copy()
arr2[2]=10
print(arr1)
print(arr2)
print(arr3)
