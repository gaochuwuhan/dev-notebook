from django.db import models

# Create your models here.

class Friend(models.Model): #定义一张新数据库表baiapp_friend
    f_name = models.CharField(max_length=120) 
    addr = models.CharField(max_length=120)
    #这里只是定义了字段名，还没有数据
    grade_id = models.IntegerField(default=6) #定义小白的朋友的班级，IntegerField代表字段是整数，默认值是6
    # born=models.IntegerField(max)