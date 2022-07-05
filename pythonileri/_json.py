# dillerin birbiri arasında iletişimini sağlayan bir yapıdır sözlük yapısına benzerdir
from asyncore import read, write
import json


person={"name":"Ahmet","languages":["python","C#"]}


print(person["name"])
print(person["languages"])
print(person["languages"][0])



person_string='{"name":"Ahmet","languages":["python","C#"]}'

result=json.loads(person_string)
print(result)

print(result["name"])
print(result["languages"])
print(result["languages"][0])

with open("person.json","r",encoding="utf-8") as f:
    resulta =f.read()

result=json.loads(resulta)

print(result)

with  open("person.json","r",encoding="utf-8") as file:
    screan=json.load(file)
    print(screan)

person_dict={
    "name":"Ali",
    "languages":["python","java"]
}

result=json.dumps(person_dict)
print(type(result))

with open("person.json","w",encoding="utf-8") as f:
    f.write(result)

person_dict=json.loads(person_string)
print(person_dict)
result=json.dumps(person_dict,indent=4,sort_keys=True)
print(result)



