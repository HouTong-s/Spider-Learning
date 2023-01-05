import redis                                           #导入redis模块
#生成StrictRedis对象
r = redis.StrictRedis(host='localhost',          #主机
                    port=6379,                       #端口
                    db=0,                             #数据库索引
                    password="123456",           #密码
                    decode_responses=True)        #解析形式：字符串
#将key为name, value为cathy的键值对添加到键为stu散列表中
r.delete("stu")
r.hset("stu", "name", "cathy")
r.hmset("stu", {"age":10, "height":1.50})          #批量添加键值对
r.hsetnx("stu", "score",100)          #如果score=100的键值对不存在，则添加
print(r.hget("stu", "name"))                   #获取散列表中key为name的值
print(r.hmget("stu", ["name", "age"]))        #获取散列表中多个key对应的值
r.hexists("stu", "name")               #判断key为name的值是否存在，此处为True
r.hdel("stu", "score")                  #删除key为score的键值对
r.hlen("stu")                            #获取散列表中键值对个数
r.hkeys("stu")                          #获取散列表中所有的key
print(r.hgetall("stu"))