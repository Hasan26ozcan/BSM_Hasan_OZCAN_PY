import requests
import json


print(requests)


result= requests.get("https://jsonplaceholder.typicode.com/todos")
print(result)
# eger cevabımızda 200 varsa o zaman bu islem de bir sıkıntının olmadıgını söylüyor

result=result.text
print(result)
print(type(result))
result=json.loads(result)
for i in result:
    if i["userId"]==1:
        print(i)
# html ile daha rahat


