from django.db import models
from django.contrib.auth.models import User
from django.contrib.humanize.templatetags import humanize
import datetime


now = datetime.datetime.now()

# Create your models here.
class Post(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, editable=True)
    updated_date = models.DateTimeField(auto_now=True)
    original_creation_date = models.DateTimeField(default=now)
    content = models.TextField()
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    public = models.BooleanField(default=True)
    image = models.ImageField(upload_to='image/%Y/%m/%d')
    likes = models.ManyToManyField(User, related_name='blogpost_like')
    blog_views = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title
    
    def get_date(self):
        return humanize.naturaltime(self.created_date)

    def get_year(self):
        return self.created_date.year

class BlogImage (models.Model):
    blog = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photoblog/static/photoblog/')
    description = models.CharField(max_length=100)
    place_tag = models.CharField(max_length=100)

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'