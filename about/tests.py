from django.test import TestCase
from about.views import about
from django.urls import resolve


class HomePageTest(TestCase):

    def test_about_page(self):
        about_page = resolve('/about/')
        self.assertEqual(about_page.func, about)

    def test_home_page_status_code_is_not_404(self):
        home_page = self.client.get('/about/')
        self.assertNotEquals(home_page.status_code, 404)

    def test_home_page_status_code_is_not_500(self):
        home_page = self.client.get('/about/')
        self.assertNotEquals(home_page.status_code, 500)
