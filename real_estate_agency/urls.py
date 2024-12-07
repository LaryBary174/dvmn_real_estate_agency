from django.urls import re_path as url
from django.contrib import admin

from property import views

urlpatterns = [
    url(r'^$', views.show_flats),
    url(r'^search/$', views.show_flats),
    url(r'^admin/', admin.site.urls),
]
