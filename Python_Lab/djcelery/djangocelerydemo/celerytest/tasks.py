# Create your tasks here
from __future__ import absolute_import, unicode_literals
 
from djangocelerydemo.celery import app
 
@app.task
def add(x,y):
    return x + y
 
 
@app.task
def sub(x,y):
    return x - y