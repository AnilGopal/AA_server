from __future__ import unicode_literals

from django.test import TestCase
import unittest
from django.core.urlresolvers import reverse
from django.test.client import RequestFactory
from .views import Login



class LoginTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def setup_view(view, request, *args, **kwargs):
        """Mimic ``as_view()``, but returns view instance.
        Use this function to get view instances on which you can run unit tests,
        by testing specific methods."""

        view.request = request
        view.args = args
        view.kwargs = kwargs
        return view

    def test_list_view(self):
        request = self.factory.get('/login')
        response = Login.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        response = self.client.post(reverse('login'), {'user':"abc",'password':'abc'})
        self.assertEqual(response.status_code, 200)

    def test_sucess_login(self):
        response = self.client.post('/login', {'user':"abc",'password':'abc'})
        self.assertEqual(response.data['status'], True)

    def test_failed_login(self):
        response = self.client.post('/login', {'user':"abc2",'password':'abc2'})
        self.assertEqual(response.data['status'], False)


