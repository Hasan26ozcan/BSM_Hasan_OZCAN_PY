#yapılan herşey aynı türde olmak zorunda

import numpy as np
#çok daha az yer kaplıyorlar ve çok daha hızlı çalışıyorlar


#python listesi
pyth_list=[1,2,3,4,5,6,7,8,9]
#numpy arrayi
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])



print(arr)
print(pyth_list)
print(type(arr))
print(type(pyth_list))


py_multi=[[1,2,3],[4,5,6],[7,8,9]]
np_multi=arr.reshape(3,2,2)

#burda islemlerden sonr aekrana yazdırm olayını gösteriyor
print(py_multi)
print(np_multi)




# burda ise boyutumuzu
print(arr.ndim)
print(np_multi.ndim)

#ndim ise bize burda kaç boyutlu olduğunu gösteriyor



# burda sisteminin nasıl olduğunu gösteriyor
print(arr.shape)
print(np_multi.shape)

