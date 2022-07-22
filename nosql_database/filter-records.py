import pymongo
from bson.objectid import ObjectId
mycliend=pymongo.MongoClient("mongodb+srv://hasanozcan:1234@cluster0.boycwzf.mongodb.net/node-app?retryWrites=true&w=majority")
mydb=mycliend["node-app"]
mydbcollections=mydb["products "]

filters={"name":"samsung s5 "}


result=mydbcollections.find(filters)
for i in result:
    print(i)

print("**"*50)
result=mydbcollections.find_one(filters)
print(result)
print("//"*50)
result=mydbcollections.find_one({"_id":ObjectId("62da9a552af65b5164c8a4a0")})
print(result)
print("**"*50)
result=mydbcollections.find({
    "name":{
        "$in":["samsung s5 ","samsung s6 "]# ama burda aradıgımız şey tamamen aradıgımız şeyle aynı olmak zorunda
    }# bu degerleri içereneri getiriyor
})
for i in result:
    print(i)
print("**"*50)
result=mydbcollections.find({
    "price":{
        "$gt": 4000 # gt ise o degerden büyükse eger o degerde islem yapıyor
                    # gte ise kendisinden büyük ve kendisine eşit olan şeyleri alıyor
    }
})
for i in result:
    print(i)

print("**"*50)
result=mydbcollections.find({
    "price":{
        "$gte": 4000 # gt ise o degerden büyükse eger o degerde islem yapıyor
                    # gte ise kendisinden büyük ve kendisine eşit olan şeyleri alıyor
    }
})
for i in result:
    print(i)

print("**"*50)
result=mydbcollections.find({
    "price":{
        "$eq": 4000 # o degere eşit olanları getir
                   
    }
})
for i in result:
    print(i)

print("**"*50)
result=mydbcollections.find({
    "price":{
        "$lt": 4000 # o degerden küçük olanları getir
                   
    }
})
for i in result:
    print(i)

print("**"*50)
result=mydbcollections.find({
    "price":{
        "$lte": 4000 # o degere eşit ve ya küçük olanları getir
                   
    }
})
for i in result:
    print(i)    


print("**"*50)
result=mydbcollections.find({
    "name":{
        "$regex":"^s" # name alanı s ile başlayanları getirmesini saglıyor
                   
    }
})
for i in result:
    print(i)        