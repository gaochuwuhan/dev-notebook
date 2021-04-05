from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name='分类',max_length=10)
class Article(models.Model):
    title = models.CharField(verbose_name="标题名",max_length=100)
    vnum = models.IntegerField(verbose_name="浏览量") #verbose_name代表表头名
    content = models.TextField(verbose_name="内容")
    category = models.ForeignKey(to=Category,on_delete=models.CASCADE,null=True,related_name='articles')