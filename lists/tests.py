from django.urls import resolve
from django.test import TestCase
from lists.views import home_page

from django.http import HttpRequest
from django.template.loader import render_to_string

# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        #self.assertTrue(html.startswith('<html>'))
        #self.assertIn('<title>To-Do list</title>', html)
        #self.assertTrue(html.strip().endswith('</html>'))
        expect_html = render_to_string('home.html')
        self.assertEqual(html, expect_html)
    
    def test_home_page_can_save_a_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_tesxt'] = 'A new list item'

        response = home_page(request)
        self.assertIn('A new list item', response.content.decode())


