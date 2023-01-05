import redis        #导入redis模块
#host是redis主机，端口是6379，数据库索引为0，密码
r = redis.StrictRedis(host='localhost', port=6379, db=0, password="123456")
#将键值对存入redis缓存，key是"name", value是"cathy"
r.set('name', "cathy")
#取出键name对应的值
print(r['name'])
print(r.get('name'))