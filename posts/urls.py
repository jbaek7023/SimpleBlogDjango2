from django.conf.urls import url
from django.contrib import admin
from posts import views as post_views

app_name = "posts"

urlpatterns = [
    url(r'^$', post_views.post_home),
    url(r'^detail/(?P<id>\d+)/', post_views.detail, name='detail'),
    url(r'^create/', post_views.post_create),
    url(r'^edit/(?P<id>\d+)/', post_views.post_update),
]
