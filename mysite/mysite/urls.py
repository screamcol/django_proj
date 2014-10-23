from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from views import hello, current_datetime, hours_ahead, display_meta
from books import views
from contact import views_contact
admin.autodiscover()

urlpatterns = patterns('',
    (r'^hello/$', hello),
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^search/$', views.search),
    (r'^http_info/$', display_meta),
    (r'^contact/$', contact),
    (r'^thanks/$', contact),
    (r'^thanks/$', thanks),
    (r'^admin/$', include(admin.site.urls)),)

urlpatterns += staticfiles_urlpatterns()

