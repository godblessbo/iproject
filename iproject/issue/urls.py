from django.conf.urls import patterns, url
from issue import views

# do not put issue in front of issue/dummy


urlpatterns = patterns('',
                       url(r'^$', views.issue),
                       url(r'home', views.issue),
                       url(r'dummy', views.dummy),
                       url(r'config', views.settings),
                       )
