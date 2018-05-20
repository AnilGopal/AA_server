# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from member.models import Member

# Create your models here.


class Promo(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    title = models.CharField(max_length=50)
    validtill = models.DateTimeField(null=True)
    amount = models.IntegerField(null=False)


class PromoPurchase(models.Model):
    promo = models.ForeignKey(Promo, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

