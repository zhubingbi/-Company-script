from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^addUser/', register),
    url(r'^register_phone/', register_phone),
]