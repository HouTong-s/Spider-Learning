# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class QidianHotPipeline:
    def process_item(self, item, spider):
        #判断小说形式是连载还是完结
        if item["form"] == "连载":              #连载的情况
            item["form"] = "LZ"                 #替换为简称
        else:
            item["form"] = "WJ"
        return item

#去除重复类型的Item Pipeline，类型为玄幻、都市之类的
class DuplicatesPipeline(object):
    def __init__(self):
        #定义一个保存类型的集合
        self.type_set = set()
    def process_item(self, item, spider):
        if item['type'] in self.type_set:
            #抛弃重复的Item项
            raise DropItem("查找到重复类型的项目： %s"%item)
        else:
            self.type_set.add(item['type'])
        return item

#将数据保存于文本文档中的Item Pipeline
class SaveToTxtPipeline(object):
    #file_name = "hot.txt"    文件名称
    file = None                               #文件对象
    #获取配置中的FILE_NAME变量
    @classmethod
    def from_crawler(cls,crawler):
        cls.file_name = crawler.settings.get("FILE_NAME","hot2.txt")
        return cls()
    #Spider开启时，执行打开文件操作
    def open_spider(self, spider):
        #以追加形式打开文件
        self.file = open(self.file_name, "a", encoding="utf-8")
    #数据处理
    def process_item(self, item, spider):
        #获取item中的各个字段，将其连接成一个字符串
        # 字段之间用分号隔开
        # 字符串末尾要有换行符\n
        novel_str = item['name']+"; "+\
                    item["author"]+"; "+\
                    item["type"]+"; "+\
                    item["form"]+"\n"
        #将字符串写入文件中
        self.file.write(novel_str)
        return item
    #Spider关闭时，执行关闭文件操作
    def close_spider(self, spider):
        #关闭文件
        self.file.close()


#导入MySQL库
import MySQLdb
#将数据保存于MySQL的Item Pipeline
class MySQLPipeline(object):
    #Spider开启时，获取数据库配置信息，连接MySQL数据库服务器
    def open_spider(self, spider):
        #获取配置文件中MySQL配置信息
        db_name = spider.settings.get("MYSQL_DB_NAME", "pachong")#数据库名称
        host = spider.settings.get("MYSQL_HOST", "localhost")    #主机地址
        user = spider.settings.get("MYSQL_USER", "root")          #用户名
        pwd = spider.settings.get("MYSQL_PASSWORD", "houzipashu.123")       #密码
        #连接MySQL数据库服务器
        self.db_conn = MySQLdb.connect(db=db_name,
                                    host=host,
                                    user=user,
                                    password=pwd,
                                    charset="utf8")
        #使用cursor()方法获取操作游标
        self.db_cursor =  self.db_conn.cursor()

    #将数据保存于MySQL数据库
    def process_item(self, item, spider):
        #获取item中的各个字段，并保存于元组中
        values = (item['name'],
                item["author"],
                item["type"],
                item["form"])
        #设计插入操作的SQL语句
        sql  = 'insert  into hot(name, author, type, form)values(%s, %s, %s, %s)'
        #执行SQL语句，实现插入功能
        self.db_cursor.execute(sql, values)
        return item

    #Spider关闭时，执行数据库关闭工作
    def close_spider(self, spider):
        self.db_conn.commit()                                 #提交数据
        self.db_cursor.close()                                #关闭游标
        self.db_conn.close()                                  #关闭数据库


import pymongo                               #导入pymongo库
#将数据保存于MongoDB的Item Pipeline
class MongoDBPipeline(object):
    #Spider开启时，获取数据库配置信息，连接MongoDB数据库服务器
    def open_spider(self, spider):
        #获取配置文件中MongoDB的配置信息
        host = spider.settings.get("MONGODB_HOST", "localhost")  #主机地址
        port = spider.settings.get("MONGODB_PORT",27017)         #端口
        db_name = spider.settings.get("MONGODB_NAME", "pachong")  #数据库名称
        collection_name = spider.settings.get("MONGODB_COLLECTION", "hot")
                                                                    #集合名称
        #连接MongoDB，得到一个客户端对象
        self.db_client = pymongo.MongoClient(host=host, port=port)
        #指定数据库，得到一个数据库对象
        self.db = self.db_client[db_name]
        #指定集合，得到一个集合对象
        self.db_collection = self.db[collection_name]

    #将数据存储于MongoDB数据库中
    def process_item(self, item, spider):
        #将item转换为字典类型
        item_dict = dict(item)
        #将数据插入到集合中
        self.db_collection.insert_one(item_dict)
        return item

    #Spider关闭时，执行数据库关闭工作
    def close_spider(self, spider):
        self.db_client.close()
        #关闭数据库连接

import redis                 #导入Redis库
#将数据保存于Redis的Item Pipeline
class RedisPipeline(object):
    #Spider开启时，获取数据库配置信息，连接Redis数据库服务器
    def  open_spider(self, spider):
        #获取配置文件中Redis配置信息
        host = spider.settings.get("REDIS_HOST")               #主机地址
        port = spider.settings.get("REDIS_PORT")               #端口
        db_index = spider.settings.get("REDIS_DB_INDEX")     #索引
        db_psd = spider.settings.get("REDIS_PASSWORD")       #密码
        #连接Redis，得到一个连接对象
        self.db_conn = redis.StrictRedis(host=host, port=port, db=db_index ,
        password=db_psd,decode_responses=True)

    #将数据存储于Redis数据库中
    def  process_item(self, item, spider):
        #将item转换为字典类型
        item_dict = dict(item)
        #将item_dict保存于key为novel的列表中
        self.db_conn.rpush("novel", str(item_dict))
        return item
    #Spider关闭时，执行数据库关闭工作
    def  close_spider(self, spider):
        #关闭数据库连接
        self.db_conn.connection_pool.disconnect()