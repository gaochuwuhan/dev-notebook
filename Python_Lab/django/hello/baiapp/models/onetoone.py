from django.db import models

class Account(models.Model):
    username = models.CharField(verbose_name="银行卡用户名",null=True,blank=True,max_length=64)
    password = models.CharField(verbose_name="密码",null=True,blank=True,max_length=64)

class Contact(models.Model):
    mobile = models.CharField(verbose_name="telephone number",max_length=20,null=True)
    account = models.OneToOneField(Account,on_delete=models.CASCADE,related_name='contact_account')