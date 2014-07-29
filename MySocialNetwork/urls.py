from django.conf.urls import patterns, url, include
from MySocialNetwork import views
from MySocialNetwork.models import User

urlpatterns = patterns('', 
                       url(r'^$', views.index, name='index'), 
                       #url(r'^(?P<from_user>\.*)/$',views.users,name = 'users'),
                       url(r'^(?P<username>\w+)/followers/$',views.followers,name = 'followers'),
                       url(r'^(?P<username>\w+)/following/$',views.following,name = 'following'),
                       
                       
)  