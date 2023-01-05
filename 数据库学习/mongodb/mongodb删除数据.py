import pymongo                                    #导入pymongo库

db_client = pymongo.MongoClient()

db = db_client.pachong
print(db)
db_collection = db["hot"]

result = db_collection.delete_one({"name":"太初"})
print(result)
print(result.raw_result)

result = db_collection.delete_many({"type":"历史"})
print(result)
print(result.raw_result)

db_client.close()