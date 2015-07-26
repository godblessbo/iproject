from django.conf.urls import patterns, url
from workspace import views

# do not put issue in front of issue/dummy


urlpatterns = patterns('',
                       url(r'^issue/$', views.issue_config),
                       url(r'^dummy/issue/$', views.dummyissue),
                       )
