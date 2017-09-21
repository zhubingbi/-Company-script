# coding=utf-8
from django.db import models

# Create your models here.


class AdminUser(models.Model):
    username = models.CharField(max_length=32, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='密码')
    phone = models.CharField(max_length=16, verbose_name='手机号')

    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(upload_to='upload_imgs/')
