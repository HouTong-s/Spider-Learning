import redis                                           #导入redis模块
#生成StrictRedis对象
r = redis.StrictRedis(host='localhost',          #主机
                    port=6379,                       #端口
                    db=0,                             #数据库索引
                    password="123456",           #密码
                    decode_responses=True)        #设置解码
r.set('name', "cathy")                     #将值为"cathy"的字符串赋给键name
r.set("age",10)                                       #将10赋给age键
r.setnx("height",1.50)                     #如果键height不存在，则赋给值1.50
r.setnx("height",2) 
r.mset({"score1":100, "score2":98})                #批量设置
r.get("name")                                          #获取键为name的值
r.mget(["name", "age"])                               #批量获取键为name和age的值
r.append("name", "good")                              #向键为name的值后追加good
print(r.mget(["name", "age", "height", "score1", "score2"]))