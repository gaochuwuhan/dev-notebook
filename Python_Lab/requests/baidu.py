import json

import requests

res=requests.get("http://www.baidu.com")
print (res.status_code,res.content)#以二进制输出
