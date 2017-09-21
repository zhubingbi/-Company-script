# coding:utf-8
from django.db import models
from teacher.models import Teacher
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.CharField(max_length=8)
    grade = models.CharField(max_length=64)
    teacher = models.ManyToManyField(Teacher)

    #def __unicode__(self):
      #  return '%s, %s' %(self.name, self.age)

