def my_decorator(func):
    def wrapper(name):
        print("fonksiyondan önceki islemler")
        func(name)
        print("fonksiyondan sonraki islemler")
    return wrapper

def sayhello(name):
    print("hello",name)    

def saygreeting(name):
    print("greeting",name)

a=my_decorator(sayhello)
a("ah")
print("**"*50)
b=my_decorator(saygreeting)
b("met")

print("**"*50)
@my_decorator
def sayHello1(name):
    print("hello",name)

sayHello1("ahmet")


import math
import time

def calculate_time(func):
    def woric(*a):
        start=time.time()
        time.sleep(1)
        func(*a)
        finish=time.time()
        sayi=finish-start
        print(sayi)
    return woric

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))


@calculate_time
def faktoriyel(number):
    print(math.factorial(number))


def toplama(a,b):
    print(a+b)


print("**"*50)
usalma(2,3)
faktoriyel(4)
print("**"*50)
week= calculate_time(toplama)
week(3,4)


