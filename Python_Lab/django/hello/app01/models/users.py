from django.db import models

class User(models.Model):
    genders = (
        (1,'男'),(2,'女')
    )   #添加一个choice,元组里的序号是存在数据库里的，男女是渲染给前端的

    name = models.CharField(max_length=10,verbose_name='名字')
    phone = models.CharField(max_length=11,verbose_name='手机号')
    gender = models.IntegerField(choices=genders,verbose_name='性别')
    pwd = models.CharField(verbose_name='密码',max_length=64)

    def __str__(self):
        return self.name