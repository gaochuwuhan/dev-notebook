## 准备 celery = "==4.4.2"  redis = "==3.5.3"   flower

# 原理
    celery_app下的：
    app文件是一个简单的任务发布文件 运行celery worker执行者进程要在celery_app下， celery -A app worker -l=info
    worker.py 是发布任务的文件 ,直接执行python worker.py即可

    设定一个cron_job 这个文件既是发布者又是执行者，对于flower来说发布者和执行者都要运行才能监控到
    即在celery_app文件夹下，
    先执行发布者： 
    celery beat -A cron_tasks -l=info &  #进程放到后台，在执行目录下会产生一个celerybeat-schedule二进制文件和一个celerybeat.pid进程文件
    再执行执行者：
    celery worker -A cron_tasks -l=info  #会显示任务执行的INFO结果

    开发环境可以执行如下只开一个worker进程：
    celery worker -A cron_tasks -B -l info 

## flower 监控
    pip安装flower或者容器，执行 flower --broker:redis://127.0.0.1:6379/0