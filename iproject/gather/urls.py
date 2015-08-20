from django.conf.urls import patterns, url
from gather import views

urlpatterns = patterns('',
                       url(r'showPage', views.showPage),
                       url(r'getgrid', views.getgrid),
                       url(r'dummygrid', views.dummygrid),
                       url(r'linkurl', views.linkurl),
                       )
