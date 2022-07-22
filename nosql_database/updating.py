import pymongo
from bson.objectid import ObjectId
mycliend=pymongo.MongoClient("mongodb+srv://hasanozcan:1234@cluster0.boycwzf.mongodb.net/node-app?retryWrites=true&w=majority")
mydb=mycliend["node-app"]
mydbcollections=mydb["products "]

# results=mydbcollections.find()
# for i in results:
#     print(i)

# print("Güncellemeden sonra".center(50,"*"))
# result=mydbcollections.update_one({"name":"samsung s6 "},{"$set":{"name":"iphone 7","price":1345600,"description":"güzel telefon"}})
results=mydbcollections.find()

for i in results:
    print(i)

query={"name":"samsung s12 "}
newvalues={"$set":{"name":"iphone 20 s ultra","price":40000,"description":"pahalı telefon"}}


result=mydbcollections.update_many(query,newvalues)

print(f"{result.modified_count} tane deger degistirilmiştir")# kaç tane degerin degistiğini bize söylüyor
results=mydbcollections.find()


results=mydbcollections.find()

for i in results:
    print(i)










