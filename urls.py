from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # url(r'^web/',include('xiaobai_web.urls')),
    url(r'^app/', include('xb.urls')),
    url(r'^admin/', include(admin.site.urls)),
]