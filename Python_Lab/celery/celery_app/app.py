from celery import Celery

celery_tasks=Celery('app',broker='redis://localhost:6379/0',backend='redis://localhost')  #broker是存放消息队列的，backend是存储结果的地方

@celery_tasks.task #task()把任务（函数）装饰成异步
def add(x,y):
    return x + y