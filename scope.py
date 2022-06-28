#global scop
x = "global x"

def functions():
    #local scop
    x="local x"
    print(x)
functions()
print(x)
#####################################
name ="çınar"

def changeName(new_name):
    name=new_name
    print(name)


changeName("ada")
print(name)

######################################
print("**"*50)
name="global String"
def greeting(name):
    name="çınar"

    def hello(name):
        name=f"hello {name} "
        print(name)
    hello(name)
    print(name) 


greeting(name)
print(name)
#########################################

x=50
def test(x):
    print("x: ",x)

    x=100
    print("change to x: ",x)


test(x)
print(x)


y=50
def test():
    global y #eger y yi global olarka fonksiyonda kullanmak istiyorsak o zaman
    #y i asla oraya göndermemeliyiz aksi taktirde global olarak orda tanımlayamayız
    print("x: ",y)

    y=100
    print("change to x: ",y)

test()
print(y)



name="mehmet"
names=input("yeni isminizi giriniz: ")
def funcwrite(names):
    global name
    name=names
    print(f"chance name {name} ")

funcwrite(names)
print(name)









