from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name='分类',max_length=10) #verbose_name参数用于设置字段的别名
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(verbose_name='标签名字',max_length=10)
    created_name = models.DateTimeField()

    def __str__(self):
        return self.name
class Article(models.Model):
    title = models.CharField(verbose_name="标题名",max_length=100)
    vnum = models.IntegerField(verbose_name="浏览量") #verbose_name代表表头名
    content = models.TextField(verbose_name="内容")
    category = models.ForeignKey(to=Category,on_delete=models.CASCADE,related_name='articles_category')    #related_name是反向查找
    tags = models.ManyToManyField(to=Tag,related_name='articles_tag') #添加一个多对多字段，一本书可能有多个tag，一个tag也可以有多本书

    def __str__(self):
        return self.title


    