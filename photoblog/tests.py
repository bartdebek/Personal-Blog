from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):
    def setUp(self):
        url = reverse('photoblog:index')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'photoblog/home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Strona Główna')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'I should not be here')
    

