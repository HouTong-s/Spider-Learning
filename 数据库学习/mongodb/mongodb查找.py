import pymongo                                    #导入pymongo库

db_client = pymongo.MongoClient()

db = db_client.pachong
print(db)
db_collection = db["hot"]

result = db_collection.find_one({"name":"帝国的崛起"})
print(result)

cursor = db_collection.find({})#查找所有记录
print(cursor)
for one in cursor:                          
        print(one)

print()
cursor = db_collection.find({"type":"历史"})#查找type为“历史”的记录
print(cursor)
for one in cursor:                          
        print(one)

db_client.close()