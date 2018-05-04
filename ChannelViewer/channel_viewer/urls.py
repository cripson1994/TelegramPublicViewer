from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.main, name='index'),
]

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]