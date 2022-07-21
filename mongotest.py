import pymongo
client = pymongo.MongoClient("mongodb+srv://santuhappy:9028399463@santosh.q3gvbzg.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d =  {
    "name" : "santosh",
    "email" : "santuhappy123@gmail.com",
    "surname" : "sattigeri"

}

d =  {
    "name" : "santosh",
    "email" : "santuhappy123@gmail.com",
    "surname" : "sattigeri"

}

d =  {
    "name" : "santosh",
    "email" : "santuhappy123@gmail.com",
    "surname" : "sattigeri"

}
d =  {
    "name" : "santosh",
    "email" : "santuhappy123@gmail.com",
    "surname" : "sattigeri"

}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )