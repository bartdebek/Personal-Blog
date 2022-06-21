import datetime

from django.db import models
from django.contrib.auth.models import User
from django.contrib.humanize.templatetags import humanize
from django.template.defaultfilters import slugify

from jupyterlab_server import slugify


now = datetime.datetime.now()

# BLOG POSTS
class Post(models.Model):
    created_date = models.DateTimeField(default=now) 
    # Not using created_date = models.DateTimeField(auto_now_add=True)
    # because posts are migrated form other site 
    # and original creation date has to be preserved
    updated_date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    public = models.BooleanField(default=True)
    image = models.ImageField(upload_to='image/%Y/%m/%d')
    blog_views = models.IntegerField(default=0)


    def slug(self):
        return slugify(self.title)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title
    
    def get_date(self):
        return humanize.naturaltime(self.created_date)

    def get_year(self):
        return self.created_date.year

# BLOG IMAGES - unused
class BlogImage (models.Model):
    blog = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photoblog/static/photoblog/')
    description = models.CharField(max_length=100)
    place_tag = models.CharField(max_length=100)

# BLOG COMMENTS
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