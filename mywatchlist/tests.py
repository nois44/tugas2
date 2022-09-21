from django.test import TestCase, Client
from django.urls import resolve

# Create your tests here.
class TestCaseResponse(TestCase):
    def test_watchlist_url_exist(self):
        response = Client().get("http://localhost:8000/mywatchlist/", follow=True)
        self.assertEqual(response.status_code,200)
    
    def test_watchlist_html_url_exist(self):
        response = Client().get("http://localhost:8000/mywatchlist/html/", follow=True)
        self.assertEqual(response.status_code,200)

    def test_watchlist_json_url_exist(self):
        response = Client().get("http://localhost:8000/mywatchlist/json/", follow=True)
        self.assertEqual(response.status_code,200)

    def test_watchlist_xml_url_exist(self):
        response = Client().get("http://localhost:8000/mywatchlist/xml/", follow=True)
        self.assertEqual(response.status_code,200)