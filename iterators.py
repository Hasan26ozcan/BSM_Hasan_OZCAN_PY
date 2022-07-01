from email import iterators
from operator import ne


liste=[1,2,3,4,5,6]


for i in liste:
    print(i)
# burada i nin yaptığı islem iterators ile benzer şeylerdir

print(dir(liste))
print("**"*50)
iterator=iter(liste)

print(iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print("//"*50)
for x in liste:
    print(x)
print("00"*60)
iterator=iter(liste)

while(True):
    try:
        sayi= next(iterator)
    except Exception as a:
        print("sistemdeki herşey ekrana başarıyla yazdırılmıştır")
        break
    else:
        print(sayi)




class mynumbers:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop
    def __iter__(self): #bizim burda for döngüsünde çalışmasını saglayan şey budaki __iter__ etodu olarka söyleyebiliriz
        return self

    def __next__(self):
        if(self.start<=self.stop):
            x=self.start
            self.start+=1
            return x
        else:
            raise StopIteration


liste=mynumbers(10,29)
iteratorsa=liste.__iter__()
print(iteratorsa.__next__())
print(iteratorsa.__next__())
print(iteratorsa.__next__())
print(iteratorsa.__next__())
print(iteratorsa.__next__())
print(iteratorsa.__next__())
print(iteratorsa.__next__())
print(iteratorsa.__iter__())
print("888"*40)
for x in liste:
    print(x)
print("+++++"*20)
liste=mynumbers(10,29)

iteration=liste.__iter__()
while True:
    try:
        x=iteration.__next__()
    except StopIteration :
        print("hatayla karşılaştık upppsssss....")
        break
    else:
        print(x)


