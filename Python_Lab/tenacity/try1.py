import random
import requests
import json
from tenacity import after_log, before_log, retry, stop_after_attempt, wait_exponential

import logging



class PlatTask(HttpPlatBase):
    """description"""

    def __init__(self,task_id,path):
        self.task_id = task_id
        self.times_out = 5
        self.path = path
        super().__init__(self.path)

    '''向中台发起task结果轮询'''

    def get_task_from_plat(self):
        res =  self.get_all()
        return res

    def get_task_state(self):
        task = self.get_task_from_plat()
        return task["state"]

    @retry(
        stop=stop_after_attempt(100),
        wait=wait_exponential(multiplier=1, min=1, max=10),
        before=before_log(logger, logging.INFO),
        after=after_log(logger, logging.WARN),
    )
    def wait_for_task_start(self):
        state = self.get_task_state()
        if state == "not_exist":
            logger.error("任务不存在")
            raise ValueError("任务不存在")

    @retry(
        stop=stop_after_attempt(600),
        wait=wait_exponential(multiplier=1, min=1, max=10),
        before=before_log(logger, logging.INFO),
        after=after_log(logger, logging.WARN),
    )
    def task_state(self):
        state = self.get_task_state()
        if state == "beginning":
            logger.error("任务进行中")
            raise ValueError("任务进行中")
        return state

    def is_task_successed(self):

        self.wait_for_task_start()
        state = self.task_state()
        if state not in ("success", "failed"):
            logger.error(f"task {self.task_id} 结果: {state}")  #not_exist或beginning
        else:
            logger.info(f"task {self.task_id} 结果: {state}")
        # result={"result":state}
        return state   #返回True或flase
