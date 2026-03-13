from django.test import TestCase, Client
from django.urls import reverse


class ArticleViewTest(TestCase):
    def test_article_list_status_code(self):
        client = Client()
        response = client.get(reverse('article_list'))
        self.assertEqual(response.status_code, 200)
