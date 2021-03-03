# from __future__ import absolute_import, unicode_literals

from celerytest.tasks import add
import time

res=add.delay(2,4)
print(res.id,res.get())