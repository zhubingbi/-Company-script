# coding:utf-8
from django.contrib import admin
from models import Student

class StudentAdmin(admin.ModelAdmin): # 定义一个类来表述指定的admin样式
    # 在admin的列表展示过程中列出指定字段
    list_display = ['id','name', 'age', 'gender']
    # 在admin的列表展示过程中添加搜索功能
    search_fields = ['name', 'gender']
    # 过滤器，以gender为过滤
    list_filter = ['gender']
    # 排序
    ordering = ['id']
# Register your models here.
admin.site.register(Student, StudentAdmin)
# 在安装表的同时安装样式