# coding:utf-8
from django.db import models


# Create your models here.
class Classes(models.Model):
    name = models.CharField(max_length=32, verbose_name='班级名称')
    description = models.TextField(blank=True, null=True, verbose_name='班级描述')

    def __unicode__(self):
        return self.name