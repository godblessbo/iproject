from django.conf.urls import patterns, url


# do not put gather in front of gather/dummy


urlpatterns = patterns('',
                       url(r'showPage', 'dashboard.views.showPage'),
                       )
