import pymongo                                    #导入pymongo库
#方式一：使用默认的host和port
db_client = pymongo.MongoClient()

db = db_client.pachong
#或者db = db_client["pachong"]
print(db)
db_collection = db["hot"]
novel={'name': '太初',                                    #名称
        'author': '高楼大厦',                               #作者
        'form': '连载',                                      #形式
        'type': '玄幻'                                       #类型
        }
result = db_collection.insert_one(novel)#插入单个值
print(result)
print(result.inserted_id)
novel1={'name': '丰碑杨门',                               #名称
        'author': '圣诞稻草人',                             #作者
        'form': '连载',                                      #形式
        'type': '历史'                                       #类型
        }
novel2={'name': '帝国的崛起',                             #名称
        'author': '终极侧位',                               #作者
        'form': '连载',                                      #形式
        'type': '都市'                                       #类型
        }
result = db_collection.insert_many([novel1, novel2])#插入多个值
print(result)
db_client.close()
#方式二：自定义host和port参数
#db_client = pymongo.MongoClient(host="localhost", port=27017)


#方式三：使用标准的URI连接语法
#db_client = pymongo.MongoClient('mongodb://localhost:27017/')