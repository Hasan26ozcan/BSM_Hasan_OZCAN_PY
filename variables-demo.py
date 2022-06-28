"""
1- bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz
 müşteri adı
 müşteri soyadı
 müşteri  ad+ soyadı
 müşteri cinsiyeti
 müşteri tc kimlik
 müşteri doğum yılı
 müşteri adresi
 müşteri yaşı
"""

from multiprocessing import managers


customername="ahmet"
customersurname="şeker"
customer=customername+" "+customersurname
customers=True # True-> erkek olarak düşünüyoruz o yüzden true yaptık
customertc="12345678999"
customerbirtdate=2003
customeradres="istanbul kadıköy"
customerage=2022-customerbirtdate

print(customername)
print(customersurname)
print(customer)
print(customers)
print(customertc)
print(customerbirtdate)
print(customeradres)
print(customerage)
"""
2 -Aşağıdaki siparişlerin toplam bigisini hesaplayınız: 
Sipariş 1 => 110 TL
Sipariş 2 => 1100.5 TL
Sipariş 3 => 356.95 TL
"""
sip1=110
sip2=1100.5
sip3=356.95

siptoplam=sip1+sip2+sip3
print("Toplam değer: ",siptoplam)
