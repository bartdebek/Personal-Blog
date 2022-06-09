from django.views.generic import ListView,YearArchiveView
from matplotlib.style import context
from photoblog.models import Post,Comment
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,get_object_or_404
from .forms import CommentForm

# Home page
def HomeView(request):
    latest_posts_list = Post.objects.order_by('-created_date')[:5]
    comments = Comment.objects.filter(active=True)
    template = loader.get_template('photoblog/home.html')
    context = {
        'latest_posts_list': latest_posts_list,
        'comments' : comments,
    }

    return HttpResponse(template.render(context, request))

# Archive page
class ArticleYearArchiveView(YearArchiveView):
    queryset = Post.objects.all()
    date_field = "original_creation_date"
    make_object_list = True
    allow_future = True
    

# Post detail page
def post_detail(request,pk):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post,pk=pk)
    comments = post.comments.filter(active=True)
    new_comment = None
    blog_object=Post.objects.get(pk=pk)
    blog_object.blog_views=blog_object.blog_views+1
    blog_object.save()
    
# Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        }

    return render(request, template_name, context)

