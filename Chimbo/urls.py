from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
from login import views as login_views
from notes import views as notes_views

admin.autodiscover()

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', login_views.welcome),
    url(r'^login/$', login_views.loginView),
    url(r'^signup/$', login_views.signUp),
    url(r'^dashboard/$', notes_views.dashboard),
    url(r'^courses/$', notes_views.courseList),
    url(r'^modules/$', notes_views.courseView),
    url(r'^notes/$', notes_views.noteView)
]
"""
urlpatterns += [('', (
    r'^static/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': 'static'}
))]
"""