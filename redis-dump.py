import redis
r = redis.Redis(host='localhost', port=6379, db=0)
for key in r.scan_iter():
       print(key)