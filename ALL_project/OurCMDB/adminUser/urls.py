# coding=utf-8
from django.conf.urls import include, url
from views import *

urlpatterns = [
    url(r'^index/', index),
    url(r'^login/$', login),
    url(r'^logout/', logout),
]