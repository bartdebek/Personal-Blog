from django.urls import path
from .views import ArticleYearArchiveView
from . import views

app_name = 'photoblog'

urlpatterns = [
    path('',views.home_view, name='index'),
    path('archive/<int:year>/',ArticleYearArchiveView.as_view(),name='post_archive_year'),
    path('post_detail/<int:pk>/',views.post_detail,name='post_detail'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('profile/',views.profile_page,name='profile'),
    path('signout/',views.signout,name='signout'),
]
