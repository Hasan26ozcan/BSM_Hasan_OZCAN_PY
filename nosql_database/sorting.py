from os import name
import pymongo
from bson.objectid import ObjectId
mycliend=pymongo.MongoClient("mongodb+srv://hasanozcan:1234@cluster0.boycwzf.mongodb.net/node-app?retryWrites=true&w=majority")
mydb=mycliend["node-app"]
mydbcollections=mydb["products "]

result=mydbcollections.find()
#result=result.sort("name",-1)#
#result=result.sort("price",1)#bu ikisini aynı tek satırda yapalım

result=result.sort([("name",1),("price",-1)])

for i in result.sort("name",-1):# yukarıdan aşağıya artarak olan 1 aşağıdak yukarıya artarak olan -1
    print(i)

