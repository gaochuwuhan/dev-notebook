## 准备 celery = "==4.4.2"  redis = "==3.5.3"

# 原理
    celery_app下的：
    app文件是一个简单的任务发布文件 运行celery进程命令要在celery_app下， celery -A app worker -l=info
    worker 是执行任务的文件 ,直接执行python worker.py即可