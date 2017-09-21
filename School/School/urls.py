"""School URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from student import views as s_v
from teacher import views as t_v
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^student/', s_v.student),
    url(r'^addData/', s_v.addData),
    url(r'^upData/', s_v.upData),
    url(r'^delData/', s_v.delData),
    url(r'^$', t_v.index),
    url(r'^register/', t_v.loveRegister),
    url(r'^ajaxTest/', t_v.ajaxTest),
]
