from django.views.generic import ListView,YearArchiveView,CreateView
from matplotlib.style import context
from photoblog.models import Post,Comment
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,get_object_or_404
from .forms import CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# HOME PAGE
def home_view(request):
    latest_posts_list = Post.objects.order_by('-created_date')[:5]
    comments = Comment.objects.filter(active=True)
    template = loader.get_template('photoblog/home.html')
    context = {
        'latest_posts_list': latest_posts_list,
        'comments' : comments,
    }

    return HttpResponse(template.render(context, request))

# ARCHIVE PAGE
class ArticleYearArchiveView(YearArchiveView):
    queryset = Post.objects.all()
    date_field = "created_date"
    make_object_list = True
    allow_future = True
    

# POST DETAIL PAGE
def post_detail(request,pk):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post,pk=pk)
    # COMMENTS
    comments = post.comments.filter(active=True)
    new_comment = None
    # VIEWS
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

# SIGN UP PAGE
class SignUpView(CreateView):

    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# PROFILE PAGE
@login_required
def profile_page(request):
    template = loader.get_template('photoblog/profile.html')
    
    return render(request, template)

# LOGGED OUT VIEW
def signout(request):
    template_name = 'logged_out.html'

    return render(request,template_name)
    
