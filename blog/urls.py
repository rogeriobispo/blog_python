from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from blog import views

urlpatterns = [
    url(r'^$', views.BlogIndex.as_view(), name="index"),
    url(r'^post/(?P<pk>[0-9]+)$', views.BlogDetail.as_view(), name="post"),
]
