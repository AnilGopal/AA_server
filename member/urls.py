from django.conf.urls import url
from django.contrib import admin
from .views import Login

urlpatterns = [
    url(r'^login/$', Login.as_view(), name='login'),
]