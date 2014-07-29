from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^users/', include('MySocialNetwork.urls')),
    url(r'^notes/', include('notes.urls')),                   
    url(r'^admin/', include(admin.site.urls)),
)