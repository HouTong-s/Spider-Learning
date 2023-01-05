import redis                                      #导入redis模块
#生成StrictRedis对象
r = redis.StrictRedis(host='localhost',     #主机
                    port=6379,                  #端口
                    db=0,                        #数据库索引
                    password="123456",      #密码
                    decode_responses=True)   #解析形式：字符串
#将"Alan Kay"（分数为1940）添加到键为hackers的有序集合中
r.delete("hackers")
r.zadd("hackers", {"Alan Kay":1940})
r.zadd("hackers", {"Sophie Wilson":1957, "Richard Stallman":1953}) #批量添加
r.zadd("hackers", {"Anita Borg":1953})
r.zadd("hackers", {"Hedy Lamarr":1914})
print(r.zrank("hackers", "Alan Kay"))         #获取"Alan Kay"在有序集合中的位置（从0开始）
print(r.zcard("hackers"))                     #获取有序集合中元素个数
print(r.zrange("hackers",0, -1))              #获取有序集合中所有元素，默认按score从小到大排序
print(r.zrevrange("hackers",0, -1))           #按score从大到小顺序获取所有元素
print(r.zrangebyscore("hackers",1900,1950))   #获取score为1900～1950之间的所有元素