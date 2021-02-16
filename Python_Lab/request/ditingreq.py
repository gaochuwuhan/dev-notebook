import requests
import logging
import json

# from psql import db
logger = logging.getLogger("django")

class Reqpar:
    def __init__(self):
        self.header=self.getheader()
        self.body=self.data()
    def getheader(self):
        api_key = "r8YpV93Y.6HRpugAluAuSNlVXiXfjpuNAhz9FTn8F"
        authorization = "Api-Key " + api_key
        headers = {"AUTHORIZATION": f"{authorization}",
        "Content-Type": "application/json"}
        return headers
    def geturl(self):
        host="http://192.168.88.163:8000/"
        path="api/vulnerability_task/"
        url=f"{host}{path}"
        # print(url)
        logging.info(url)
        return url
    def data(self):
        data={"subnets": [{"ip":"192.168.88.158"}]}
        return data

class Makereq:
    def post(self,url,body,headers):
        req=requests.post(url,json=body,headers=headers)
        # task_id=res.get("id")
        body=Reqpar().body
        res=req.json()
        id=res.get('id')
        return dict(data=body,id=id)
logging.error(Makereq().post(Reqpar().geturl(),Reqpar().body,Reqpar().header))
def assert_task(id):
    assert id

# class ScanTask:
#     def __init__(self,id):
#         self.id=id
#         self.db=db.Opdb()  #实例化数据库
#     def get_query_result(self,sql_str):
#         msg_id=self.db.doconn(sql_str)
#         return msg_id
    # def get_vu_msg_id(self):
        




