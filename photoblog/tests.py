from django.test import TestCase
from django.urls import reverse

from .models import Post,User

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
    

class PostTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')

        cls.post = Post.objects.create(
            content = 'Test text',
            title = 'Test title',
            author = cls.user
        )

    def test_post_listing(self):
        self.assertEqual(f'{self.post.content}','Test text')
        self.assertEqual(f'{self.post.title}','Test title')
        self.assertEqual(self.post.blog_views,0)
        self.assertEqual(self.post.public,True)
        