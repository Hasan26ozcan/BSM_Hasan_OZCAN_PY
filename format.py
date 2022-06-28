name ="çınar"
surname="turan"
age=36
print("my name is {} {}  ".format(name,surname))
print("my name is {1} {0}  ".format(name,surname))
#normal indekse bakicak olursak 0 1 indeksleri diye diyebiliriz ama yer degistirmek icin
# 1 0 yaparsak yer degistirmis oluruz
print("my name is {} {} and \nI am {} years old".format( name, surname,age))
print("my name is {} {} and \nI am {} years old".format( name,name,name))

result=200/700
print("the resault is {r:1.2} ".format( r=result))
#burda bu işlemi yaparken yuvarlayarak yapıyor 1.2 yaptığımızda . dan sonraki 2 değeri yazıyor
#ve o değere kadar arkasında olanları yuvarlayarak işlemi yapıyor
# öndeki değer ise önünde ne kadar alan bırakacağı ile ilgilidir
#ama bu saymaya sayının kendiside dahil . sayılar ve boşlukla beraber o öndeki sayı oluyor dikkat



print("my name is {} {} and \nI am {} years old".format( name, surname,age))
print(f"my name is {name} {surname} and \nI am {age} years old")
# bu işlem ise oranın kısa yolu
