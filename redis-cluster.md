# redis cluster
## connect
```python
from redis import RedisCluster as Redis
r=Redis(host="HOSTNAME",port=6379)
# r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
# r.get("Bahamas")
print(r.get_nodes())
```
