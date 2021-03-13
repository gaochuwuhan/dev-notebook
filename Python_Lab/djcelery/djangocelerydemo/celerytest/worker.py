# from __future__ import absolute_import, unicode_literals

from celerytest.api_tasks import add
import time

def a():
    res=add.delay(2,4)
    print(res.id,res.get())

a()