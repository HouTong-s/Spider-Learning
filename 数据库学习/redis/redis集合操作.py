import redis #导入redis模块
#生成StrictRedis对象
r = redis.StrictRedis(host='localhost',     #主机
                    port=6379,                  #端口
                    db=0,                        #数据库索引
                    password="123456",      #密码
                    decode_responses=True)   #解析形式：字符串
#将"cathy", "tom", "terry", "lili", "tom"5个元素添加到键为names的集合中
r.delete("names","names1")
r.sadd("names", "cathy", "tom", "terry", "lili", "tom")
print(r.scard("names"))                        #获取键为names的集合中的元素个数，结果为4
r.srem("names", "tom")                  #从键为names的集合中删除"tom"
print(r.spop("names"))                         #从键为names的集合中随机删除并返回该元素
#将"terry"从键为names的集合中转移到键为names1的集合中
r.smove("names", "names1", "terry")
r.sismember("names", "cathy")         #判断"cathy"是否是键为names的集合中的元素
print(r.srandmember("names"))                 #随机获取键为names的集合中的一个元素
print(r.smembers("names"))            #获取键为names的集合中的所有元素