from django.test import TestCase
from contact.views import contact
from django.urls import resolve


class ContactPostTests(TestCase):

    def test_about_page(self):
            about_page = resolve('/contact/')
            self.assertEqual(about_page.func, contact)

    def test_home_page_status_code_is_not_404(self):
            home_page = self.client.get('/')
            self.assertNotEquals(home_page.status_code, 404)

    def test_home_page_status_code_is_not_500(self):
            home_page = self.client.get('/')
            self.assertNotEquals(home_page.status_code, 500)