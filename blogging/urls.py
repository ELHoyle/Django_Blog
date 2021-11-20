from django.urls import path
from blogging.views import PostListView, PostDetailView, about_view

urlpatterns = [
    path('', PostListView.as_view(), name='blog_index'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name="blog_detail"),
    path('about/', about_view, name="blog_about" )
]
