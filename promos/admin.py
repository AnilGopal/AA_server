# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Promo,PromoPurchase

class PromoAdmin(admin.ModelAdmin):
    pass

class PromoPurchaseAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Promo, PromoAdmin)
admin.site.register(PromoPurchase, PromoPurchaseAdmin)
