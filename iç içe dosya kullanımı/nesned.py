def greeting(name):
    print("hello ",name)
    pass

print(greeting("Ali"))
print(greeting) # adresini yazdırmamızı saglıyor

sayhello=greeting

print(sayhello("Hasan"))

del greeting
# boyle birsey yaparsak bir ordaki adı siliyoruz adresi silmiyoruz

print(sayhello)



#bu isleme encapsulations diyoruz karmasık kodlarda isimizi kolaylastırıyor ve dışarıdan bağımsız olmamızı saglıyor
def outher(num1):
    print("outher")
    def inner_increment(num1):
        print("inner increment")
        return num1+1
    num2= inner_increment(num1)
    print(num1,num2)




print(outher(67))
number=outher
print(number(123))

def factorial(number):
    cor=False
    if not isinstance(number,int): # burda bize gönderilen sayının typına göre integer mi string mi olduguna 
        # göre islem yapıyor
        raise TypeError("bu integer bir sayı değildir")
    
    if not number>=0:
        raise ValueError("number 0 ve pozitif olmalıdır")
        

    def inner_factoriyal(number):
        if number<1:
            return 1
        else:
            return number*inner_factoriyal(number-1)
    factoriyal= inner_factoriyal(number)
    print(factoriyal)
print("**"*50)

factorial(5)
factorial(100)
factorial(2)


try:
    factorial("4")
except Exception as error:
    print(error)

































