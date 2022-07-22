import pymongo

myciliend=pymongo.MongoClient("mongodb+srv://hasanozcan:1234@cluster0.boycwzf.mongodb.net/node-app?retryWrites=true&w=majority")

mydb=myciliend["node-app"]
mycollesctions=mydb["products "]


# result=mycollesctions.find_one()

# print(result)
# print(type(result))

for i in mycollesctions.find({},{"_id":0,"name":1,"price":1}):
    print(i)


for i in mycollesctions.find({},{"_id":0,"name":1}):# eger boyle yaptıysak ise id,name,... degeri 0 oldugu için onu degil
    # ama geri kalanın hepsini alır
    # ama 1 yazarsak eger sadece orda 1 olanları getirir ama 0 yazarak gidersek sadece o 0 yazılan satırı çıkartır
    # ilk açıp kapattıgımız parantezler ise sql where ile aynı işlev
    print(i)
