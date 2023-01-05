import redis                                      #导入redis模块
#生成StrictRedis对象
r = redis.StrictRedis(host='localhost',     #主机
                    port=6379,                  #端口
                    db=0,                        #数据库索引
                    password="123456",      #密码
                    decode_responses=True)   #解析形式：字符串
r.delete("student")
r.lpush("student", "cathy",10)   #向键为student的列表头部添加值"cathy"和10
r.rpush("student",1.50, "女")    #向键为student的列表尾部添加值身高和性别
print(r.lrange("student",0,3))  #获取列表student中索引范围是0～3的列表
r.lset("student",1,9)             #向键为student中索引为1的位置赋值9
r.lpop("student")                  #返回并删除列表student中的首元素
r.rpop("student")                  #返回并删除列表student中的尾元素
r.llen("student")                  #获取student列表长度
print(r.lrange("student",0, -1))               #获取列表student中的所有数据