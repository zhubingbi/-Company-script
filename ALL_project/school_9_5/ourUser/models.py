# coding=utf-8
from django.db import models

class OurUser(models.Model):
    # 这个是注册必填
    phone = models.CharField(max_length=16, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='密码')
    username = models.CharField(max_length=32, verbose_name='用户名')

    # 这个交给用户自己去创建
    gender = models.CharField(max_length=16, verbose_name='性别', null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)


