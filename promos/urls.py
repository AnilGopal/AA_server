from django.conf.urls import url
from django.contrib import admin
from .views import PromosList, Purchase, PromoDetail, Transfer

urlpatterns = [
    url(r'^all/$', PromosList.as_view()),
    url(r'^detail/$', PromoDetail.as_view()),
    url(r'^buy/$', Purchase.as_view()),
    url(r'^give/$', Transfer.as_view()),
]