from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.defaults import page_not_found
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    url(r'^channel_viewer/', include('channel_viewer.urls')),
    url(r'^$', views.index, name='index'),
	url(r'^login$', views.sign_in, name='sign_in'),
	url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^404/$', page_not_found, {'exception ': Exception()}),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
