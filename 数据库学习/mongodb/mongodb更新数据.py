import pymongo                                    #导入pymongo库

db_client = pymongo.MongoClient()

db = db_client.pachong
print(db)
db_collection = db["hot"]
#查询条件
filter={"name":"帝国的崛起"}
#更新语句
update={"$set":{"type":"历史"}}
#使用update_one()方法更新文档
result = db_collection.update_one(filter, update)
print(result)
print(result.raw_result)

#查询条件
filter={"type":"历史"}
#更新语句
update={"$set":{"form":"完本"}}
#使用update_one更新文档
result = db_collection.update_many(filter, update)
print(result)
print(result.raw_result)

db_client.close()