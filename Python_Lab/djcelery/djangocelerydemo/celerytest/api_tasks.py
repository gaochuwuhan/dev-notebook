# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery.schedules import crontab

from djangocelerydemo.celery import app
 
@app.task
def add(x,y):
    return x + y
 
 
@app.task
def sub(x,y):
    return x - y

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
    crontab(minute='*/2', day_of_week='*'),
    sub.s(22, 11),
)