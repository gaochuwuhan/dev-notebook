import random
import requests
import json
from tenacity import after_log, before_log, retry, stop_after_attempt, wait_exponential

import logging

#何时retry
#默认情况下，只有函数抛出异常时才会retry。
#可以设置在制定的异常才进行retry

logging.basicConfig(level=logging.INFO) 
logger = logging.getLogger('try')

class Task:
    def __init__(self,path):
        self.path = path

    def get_data_from_django(self):  
        url=f"http://127.0.0.1:8000/baiapp/drf{self.path}"      
        response = requests.get(url=url)
        res = response.json()
        for i in res[0:]:
            if i['id']==1:
                data=i
        return data

    def get_vnum_from_django(self):
        data=self.get_data_from_django()
        vnum=data['vnum']
        return vnum
    
    retry(
        stop=stop_after_attempt(100),
        wait=wait_exponential(multiplier=1, min=1, max=10),
        before=before_log(logger, logging.INFO),  #retry之前的日志等级
        after=after_log(logger, logging.WARN),  #retry之后的日志等级
    )
    def wait_vnum_up_django(self):
        vnum = self.get_vnum_from_django()
        # if vnum == 0:
        #     logger.error("阅读量为0")
        #     raise ValueError("阅读量为0")

    @retry(
        stop=stop_after_attempt(600), #尝试600次后就不尝试了
        wait=wait_exponential(multiplier=1, min=1, max=10),#开始的时候等待 2^x * 1 秒，最少等待1秒，最多10秒，之后都是等待10秒
        before=before_log(logger, logging.INFO),
        after=after_log(logger, logging.WARN),
    )    
    def get_vnum_is_growing(self):
        vnum = self.get_vnum_from_django()
        if (0 < vnum < 10):
            logger.error("阅读量增长中")
            raise ValueError("阅读量增长中")
        elif vnum==0:
            logger.error("阅读量为0")
            raise ValueError("阅读量为0")
        return vnum

    def is_finish_vnum(self):
        self.wait_vnum_up_django()
        vnum = self.get_vnum_is_growing()
        if vnum==10:
            logger.info(f"阅读量完成{vnum}")
        else:
            logger.error(f"阅读量不到10，只有 {vnum} 遗憾")
        return vnum
        

def test(path):
    return Task(path=path).is_finish_vnum()
    
print(test(path="/article"))


# first=response.json()[0]
# print (first['id'])