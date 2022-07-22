import pymongo

myciliend=pymongo.MongoClient("mongodb+srv://hasanozcan:1234@cluster0.boycwzf.mongodb.net/node-app?retryWrites=true&w=majority")

mydb=myciliend["node-app"]
mycollesctions=mydb["products "]


# result=mycollesctions.find()
# for i in result:
#     print(i)
# print("**"*50)
# results=mycollesctions.delete_one({"name":"iphone 11"})
# result=mycollesctions.find()
# for i in result:
#     print(i)

# print(f" {results.deleted_count} tane deger silinmiştir")



result=mycollesctions.find()
for i in result:
    print(i)
print("**"*50)
results=mycollesctions.delete_many({"name":"iphone 11"})#s ile başlayan degerleri silmemeizi saglıyor
result=mycollesctions.find()
for i in result:
    print(i)

print(f" {results.deleted_count} tane deger silinmiştir")




result=mycollesctions.find()
for i in result:
    print(i)
print("**"*50)
results=mycollesctions.delete_many({"name":{"$regex":"^s"}})#s ile başlayan degerleri silmemeizi saglıyor
result=mycollesctions.find()
for i in result:
    print(i)

print(f" {results.deleted_count} tane deger silinmiştir")


