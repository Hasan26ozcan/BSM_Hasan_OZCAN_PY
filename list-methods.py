from operator import le


numbers=[1,10,5,16,4,9,10]
letters=["a","g","s","b","y","a","s"]

result=min(numbers)
print(result)
result=max(numbers)
print(result)
result=min(letters)
print(result)
result=max(letters)
print(result)
result=numbers[3:6]
print(result)
numbers[4]=40
numbers.append(49)
print(numbers)
numbers.insert(3,56)
print(numbers)
numbers.insert(len(numbers),78)
print(numbers)
numbers.pop(0)
numbers.pop()
#eğer içerisine değer girmezsek o zaman en sondaki elemanı siler ama eğer içine hangi 
# indeksi girersek o zaman o indeksi siler
print(numbers)
#remove metodunda ise silmek istediğimiz değeri giriyoruz ve onu silmesini sağlıyoruz
numbers.remove(40)
print(numbers)
numbers.sort()
letters.sort()
print(numbers)
print(letters)
numbers.reverse()
letters.reverse()
print(len(numbers))
print(len(letters))
print(numbers.count(10))
print(letters.count("a"))

numbers.clear
print(numbers)



