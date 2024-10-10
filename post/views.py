from django.utils import cache
from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import (
    AllowAny
)
from django.core.cache import cache

from post.models import Post
from post.permissions import IsAnnaPermission
from post.serializers import PostSerializer


# Create your views here.

class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        cache_key = 'post-list'
        cached_data = cache.get(cache_key)
        if not cached_data:
            queryset = Post.objects.all().select_related('user')
            queryset = queryset.prefetch_related('user__groups')
            queryset = queryset.prefetch_related('user__user_permissions')
            cache.set(cache_key, queryset, timeout=60 * 3)
            return queryset
        return cached_data


class PostDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAnnaPermission]
    lookup_field = 'pk'


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
