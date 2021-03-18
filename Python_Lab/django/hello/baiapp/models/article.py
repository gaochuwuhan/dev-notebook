from django.db import models

class Article(models.Model):
    title = models.CharField(verbose_name="标题名",max_length=100)
    vnum = models.IntegerField(verbose_name="浏览量") #verbose_name代表表头名
    content = models.TextField(verbose_name="内容")