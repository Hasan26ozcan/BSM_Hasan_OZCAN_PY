#iteratordan farklı olarak yaptıgımızda bellekten 
# generator bellekte yer kaplamayan bir iterater üretiyor


def cube():
    result=[]

    for i in range(0,5):
        result.append(i**3)
    return result



kuba= cube()
print(kuba)


def cuben():

    for i in range(0,5):
        yield i**3
# generate=cuben()
# iterate=iter(generate)


# for i in generate:
#     print(i)

# print(next(generate))
# print(next(generate))
# print(next(generate))
# print(next(generate))

# print(next(iterate))
# print(next(iterate))
# print(next(iterate))
# print(next(iterate))

#burda önemli olan bir diger ayrıntı ise  yield sadece 1 kere çalışıyor sonra alttaki fora giriyor
#eger daha fazla istek fazla o zaman ona göre gidip tekrardan bir deger daha alıyor
for x in cube():
    print(x)

liste=[i**3 for i in range(0,5)]
print(liste)

list=(i**3 for i in range(0,5))
#generate oluyor bu şekilde yaptığımızda
print(list)


for x in list:
    print(x)

listesi=(1,2,3,4,5)
print(type(listesi))
print(listesi[0])
