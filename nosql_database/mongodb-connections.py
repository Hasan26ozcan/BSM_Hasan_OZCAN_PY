import pymongo


#mycliend=pymongo.MongoClient("mongodb://localhost:27017")
mycliend=pymongo.MongoClient("mongodb+srv://hasanozcan:1234@cluster0.boycwzf.mongodb.net/node-app?retryWrites=true&w=majority")
mydb=mycliend["node-app"]
mydbcollection=mydb["products "]
print(mycliend.list_database_names())
print(mydb.list_collection_names())
products={"name":"samsung s5 ","price":3000}

result=mydbcollection.insert_one(products)
print(result)
print(type(result))
print(result.inserted_id)

produclist=[
    {"name":"samsung s11 ","price":2000,"description":"iyi telefon"},
    {"name":"samsung s12 ","price":3000,"categories":["telefon","elektronik"]},
    {"name":"samsung s13 ","price":4000},
    {"prudcsname":"samsung s14 ","price":5000},
    {"name":"samsung s15 ","pricenes":6000},
    {"name":"samsung s116 ","price":7000},
    {"name":"samsung s57 ","price":8000}
]
result=mydbcollection.insert_many(produclist)
print(result.inserted_ids)




