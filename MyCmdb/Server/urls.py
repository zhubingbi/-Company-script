from django.conf.urls import url
from views import *

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^saveServer/', saveServer),
]
