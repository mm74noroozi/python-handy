from requests import session
from datetime import datetime
import json
import functools

s=session()

username="homeca"
password="MyHomeca2021"
host="http://container-registry.homeca.ir"
auth=(username, password)

def set_the_blobs(histroy):
    data=[]
    for item in history:
        data.extend(item[0])
    return set(data)

res = s.get(f"{host}/v2/_catalog",auth=auth)
if res.status_code !=200:
    raise Exception("error getting repo: check domain and user name")
for item in res.json()["repositories"]:
    if "cache" in item or 'dev' not in item:
        continue
    res2=s.get(f"{host}/v2/{item}/tags/list",auth=auth).json()
    history=[]
    for tag in res2["tags"]:
        res3=s.get(f"{host}/v2/{item}/manifests/{tag}",auth=auth).json()
        blobs=list(map(lambda x:x["blobSum"],res3["fsLayers"]))
        dict_string=res3["history"][0]["v1Compatibility"]
        created= datetime.fromisoformat(json.loads(dict_string)["created"].split(".")[0])
        history.append((blobs,created))
        print(history[-1])
    history=sorted(history,key=lambda x:x[1],reverse=True)
    maximum_length=min(len(history),3)
    excluded_blobs=set_the_blobs( history[:maximum_length])
    all_blobs=set_the_blobs(history)
    should_delete_blobs=list(all_blobs-excluded_blobs)
    # for blob in should_delete_blobs:
    #     res=s.delete(f"{host}/v2/{item}/blobs/{blob}",auth=auth)
    #     print(res)
