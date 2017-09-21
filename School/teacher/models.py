# coding:utf-8
from django.db import models
from classes.models import Classes
# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.CharField(max_length=8)
    project = models.ForeignKey(Classes)
    # 外键，表示哪个表的外键. 在多的这边写

    def __unicode__(self):
        return self.name

class Us(models.Model):
    user = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

