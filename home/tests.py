from django.test import TestCase
from home.views import get_home
from django.urls import resolve


class HomePageTest(TestCase):
    def test_home_page_resolves(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, get_home)

    def test_home_page(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, get_home)

    def test_home_page_status_code_is_not_404(self):
        home_page = self.client.get('/')
        self.assertNotEquals(home_page.status_code, 404)

    def test_home_page_status_code_is_not_500(self):
        home_page = self.client.get('/')
        self.assertNotEquals(home_page.status_code, 500)
