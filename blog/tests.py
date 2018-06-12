from .models import BlogPost
from django.test import TestCase
from blog.views import post_list
from django.urls import resolve


class BlogPostTests(TestCase):

    def test_str(self):
        test_title = BlogPost(title='My Latest Blog BlogPost')
        self.assertEqual(str(test_title),
                         'My Latest Blog BlogPost')

    def test_about_page(self):
            about_page = resolve('/blog/')
            self.assertEqual(about_page.func, post_list)

    def test_home_page_status_code_is_not_404(self):
            home_page = self.client.get('/')
            self.assertNotEquals(home_page.status_code, 404)

    def test_home_page_status_code_is_not_500(self):
            home_page = self.client.get('/')
            self.assertNotEquals(home_page.status_code, 500)

    def test_blog_page_status_code_is_ok(self):
        blog_page = self.client.get('/blog/')
        self.assertEquals(blog_page.status_code, 200)