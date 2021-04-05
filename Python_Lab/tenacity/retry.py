import requests
import tenacity import retry,stop
import logging
import json



logging.basicConfig(level=logging.INFO) 
logger = logging.getLogger('ten')


class Dstask:
    
    def __init__(self):
        self.host="test.ds.wudun.net"
        self.port=8001
      
    
    def get_headers(self):
        api_key="Api-Key rxx"
        return {"AUTHORIZATION":api_key}

    def send_request(self,path):
        url = f"http://{self.host}:{self.port}{path}"
        headers=self.get_headers()
        logger.info(f"path: {path},url: {url}")
        response=requests.get(url,headers=headers)
        res = self.get_result(response)
        return res

    def get_result(self, response):
        try:
            response_data = response.json()
        except json.JSONDecodeError:
            response_data = {}
        logger.debug(f"返回值是{str(response_data)[:100]}")
        return response_data

def get_result(path):
    
    result = Dstask().send_request(path=path)
    return result

response = get_result(path="/api/tasks/2e80e2b6-1404-4e37-8840-57d6d6e832e4")
print(response)
