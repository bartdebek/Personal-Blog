from photoblog.models import Post
from django.shortcuts import render

def popular_posts(request):
    most_popular_posts = Post.objects.order_by('-blog_views')[:5]

    return {'most_popular_posts':most_popular_posts}