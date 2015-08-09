from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^iproject/$', 'dashboard.views.home'),
                       url(r'^accounts/login/$', 'dashboard.views.sign_in_view'),
                       url(r'^iproject/login/$', 'dashboard.views.sign_in'),
                       url(r'^accounts/logout/$', 'dashboard.views.sign_out'),
                       url(r'^accounts/logon/$', 'dashboard.views.sign_up_view'),
                       url(r'^iproject/logon/$', 'dashboard.views.sign_up'),
                       url(r'^iproject/home/', 'dashboard.views.home'),
                       url(r'^iproject/workspace/', include('workspace.urls')),
                       url(r'^iproject/gather/', include('gather.urls')),
                       )
