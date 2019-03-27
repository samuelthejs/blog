from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
  path('', views.post_list, name='list'),
  path(r'create/', views.post_create),
  url(r'^(?P<id>\d+)/$', views.post_detail, name='detail'),
  url(r'^(?P<id>\d+)/edit/$', views.post_update, name='update'),
  url(r'^(?P<id>\d+)/delete/$', views.post_delete),
]