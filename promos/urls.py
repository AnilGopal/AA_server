from django.conf.urls import url
from django.contrib import admin
from .views import PromosList, Purchase, PromoDetail, Transfer

urlpatterns = [
    url(r'^all/$', PromosList.as_view(), name="all"),
    url(r'^detail/$', PromoDetail.as_view(), name="detail"),
    url(r'^buy/$', Purchase.as_view(), name="buy"),
    url(r'^gift/$', Transfer.as_view(), name="gift"),
]