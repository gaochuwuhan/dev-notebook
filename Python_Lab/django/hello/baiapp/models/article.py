from django.db import models

class Article(models.Model):
    title = models.CharField(verbose_name="标题名",max_length=100)
    vum = models.IntegerField(verbose_name="浏览量")
    content = models.TextField(verbose_name="内容")