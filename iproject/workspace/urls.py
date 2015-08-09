from django.conf.urls import patterns, url
from workspace import views

# do not put gather in front of gather/dummy


urlpatterns = patterns('',
                       url(r'^gather/$', views.gather_config),
                      # url(r'^dummy/gather/$', views.dummygather),
                       )
