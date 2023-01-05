import redis                             #导入redis模块
pool = redis.ConnectionPool(host='localhost', port=6379, password="123456",decode_responses=True)
r = redis.Redis(connection_pool=pool)
r.set('name', 'cathy')
print(r.get('name'))