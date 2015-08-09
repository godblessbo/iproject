from django.conf.urls import patterns, url
from gather import views

# do not put gather in front of gather/dummy


urlpatterns = patterns('',
                       url(r'showGatherJoinInfo', views.showGatherJoinInfo),
                       url(r'getGatherJoinInfo', views.getGatherJoinInfo),
                       url(r'dummyGatherJoinInfo', views.dummyGatherJoinInfo),

                       )
