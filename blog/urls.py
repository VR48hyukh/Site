from django.urls import path
from django.views.decorators.cache import cache_page

from . import views
from .views import PostListView

urlpatterns = [
    #path('comment/<int:pk>/', views.CreateComment.as_view(), name="create_comment"),
    #path('<slug:slug>/<slug:post_slug>/', views.PostDetailView.as_view(), name="post_single"),
    #path('<slug:slug>/', views.PostListView.as_view(), name="post_list"),
    path('', cache_page(60 * 15)(views.HomeView.as_view()), name="home"),
    path('/home', views.HomeView.as_view(), name="home"),
    path('/reciepe', views.RecipeListView.as_view(), name='reciep'),
    path('/post', views.PostListView.as_view(), name='posts'),
    path('/comment', views.CommentListView.as_view(), name='comment')
]