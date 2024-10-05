from django.urls import path

from post.views import PostListView, PostDetailApiView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailApiView.as_view(), name='post_detail')
]
