from __future__ import unicode_literals

from django.test import TestCase
import unittest
from django.core.urlresolvers import reverse
from django.test.client import RequestFactory
from .views import PromosList, PromoDetail, Purchase, Transfer
from member.models import Member
from .models import Promo

class PromosTest(TestCase):
    @classmethod
    def setUpClass(cls):
        Member(name="abc", password="abc")
        Promo(code="PROMO123", amount=1000, title="title", description="description")

    def test_all(self):
        response = self.client.get(reverse("all"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['data']), 0)

    def test_detail(self):
        response = self.client.post(reverse("detail"),
                                   {"pcode": "PROMO123", "mem": "abc"})
        self.assertEqual(response.status_code, 200)
        data = response.data
        self.assertEqual(data['amount'], 1000)
        self.assertEqual(data['code'], "PROMO123")
        self.assertEqual(data['status'], True)
        self.assertEqual(data['title'], "Promo title")

    def test_buy(self):
        response = self.client.post(reverse("buy"),
                                    {"pcode": "PROMO123", "mem": "abc"})
        self.assertEqual(response.status_code, 200)
        data = response.data
        self.assertEqual(data.status, True)

    def test_gift(self):
        response = self.client.post(reverse("gift"),
                                    {"pcode": "PROMO123", "mem": "abc","memto":"abc"})
        self.assertEqual(response.status_code, 200)

