from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from .views import IndexView


class MainViewTests(TestCase):

    def test_index_view(self):
        response = self.client.get(reverse('main:index'))
        # Check http response code is good
        self.assertEqual(response.status_code, 200)
        # Check some page text
        self.assertContains(response, "Homepage")

    def test_root_url_resolves_to_home_page_view(self):
        # Use resolve to find view function that maps to string
        match = resolve('/')
        self.assertEqual(match.func.__name__, IndexView.__name__)

    def test_about_view(self):
        response = self.client.get(reverse('main:about'))
        # Check http response code is good
        self.assertEqual(response.status_code, 200)
        # Check some page text
        self.assertContains(response, "About")
