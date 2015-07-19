from django.conf.urls import patterns, include, url
from django.contrib import admin

# do not put issue in front of issue/dummy

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^iproject/$', 'iproject.views.home', name='home'),
                       # url(r'^iproject/blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^iproject/issue/dummy', 'issue.views.dummy'),
                       url(r'^iproject/issue/settings', 'issue.views.settings'),
                       url(r'^iproject/issue/getselect', 'issue.views.getselect'),
                       url(r'^iproject/issue/home', 'issue.views.issue'),
                       url(r'^iproject/home', 'issue.views.home'),
                       )
