# Talk urls
from django.conf.urls import patterns, url
from djrestapp import views

urlpatterns = patterns(
    'djrestapp.views',
    url(r'^$', 'home'),
    url(r'^api/v1/address/$', views.post_geoaddress),
)
