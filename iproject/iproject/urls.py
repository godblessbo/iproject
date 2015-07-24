from django.conf.urls import patterns, include, url
from django.contrib import admin

from dashboard import views

# do not put issue in front of issue/dummy

urlpatterns = patterns('',

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'iproject/home/', views.home),
                       url(r'iproject/issue/', include('issue.urls')),
                       url(r'iproject/', views.home),
                       )
