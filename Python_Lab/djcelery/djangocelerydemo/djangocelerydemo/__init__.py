# 引入celery实例对象
from __future__ import absolute_import, unicode_literals
from djangocelerydemo.celery import app as celery_app
 
__all__ = ('celery_app',)
 
 
# import pymysql
# pymysql.install_as_MySQLdb()