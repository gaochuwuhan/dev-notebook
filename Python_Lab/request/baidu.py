import json
import requests

res=requests.get("http://www.baidu.com")
print (res.status_code)
print(json.loads(res.content))