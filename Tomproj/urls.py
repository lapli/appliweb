from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
##urlpatterns = patterns('tomapp.views',
##    # Examples:
##    # url(r'^$', 'Tomproj.views.home', name='home'),
##    # url(r'^blog/', include('blog.urls')),
##
##    url(r'^admin/', include(admin.site.urls)),
##    url(r'^pilo/$', 'tomapp.views.home'),
##    url(r'^pilo/$', 'home'),
##    url(r'^article/(\d+)$', 'view_article'),
##    #url(r'^article/(\d{4})/(\d{2})$', 'list_article'),
##    url(r'^home/$', 'home'),
##    url(r'^article/(?P<id_article>\d+)$', 'view_article'),
##    #url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})$', 'list_articles'),
##)
