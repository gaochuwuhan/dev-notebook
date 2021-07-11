#执行任务发布者的文件，也可以在python终端执行
from app import celery_tasks,add
import time

result=add.delay(2,3)
print(result.id,result.get())




