from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Chimbo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin//', include(admin.site.urls)),
    url(r'^index.html$', 'chApp.views.index'),
    	
)   
urlpatterns += staticfiles_urlpatterns()


