import requests
import json

data = {
    "title": "红楼"
}

url = "http://127.0.0.1:8008/baiapp/drf/django_article/8/"

res = requests.patch(url=url,json=data)
print(res.json())