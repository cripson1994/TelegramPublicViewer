from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.defaults import page_not_found

from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^channel_viewer/', include('channel_viewer.urls')),
  	url(r'^view_posts/$', views.channel_posts, name='channel_posts'),
    url(r'^search/$', views.search, name='search'),
	url(r'^view_posts/(?P<ch_name>\w{1,128})/', views.channel_posts, name='channel_page'),
	url(r'^login/$', views.login, name='login'),
	url(r'^test/$', views.create_example, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^$', views.index, name='index'), 
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^404/$', page_not_found, {'exception ': Exception()}),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
