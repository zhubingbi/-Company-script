# coding:utf-8
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=32, verbose_name='姓名')
    gender = models.CharField(max_length=32, verbose_name='性别')
    age = models.IntegerField(verbose_name='年龄')
    birthday = models.DateTimeField(verbose_name='生日')
    grade = models.CharField(max_length=32, verbose_name='班级')
    subject = models.CharField(max_length=32, verbose_name='专业')
    city = models.CharField(max_length=32, verbose_name='城市')