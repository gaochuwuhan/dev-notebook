#celery的任务文件，发布任务到消息队列redis
from celery.schedules import crontab
from app import celery_tasks

CELERY_TIMEZONE = 'Asia/Shanghai'
@celery_tasks.task 
def sub(x,y):
    return x-y

@celery_tasks.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
    crontab(minute='*/2', day_of_week='*'),
    sub.s(22, 11),
)

#定时任务用celery beat -A cron_tasks -l=info 命令开启