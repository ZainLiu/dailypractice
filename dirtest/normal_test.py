import redis

conn = redis.Redis(host='127.0.0.1',port=6379,password='')
# hellp = conn.set('hello2','zhenyu')
hellp = conn.set('hello2',2)
print(hellp)