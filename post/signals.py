from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache

from post.models import Post


@receiver(post_save, sender=Post)
def create_post(sender, instance, **kwargs):
    cache_key = 'post-list'
    cache.delete(cache_key)


@receiver(post_delete, sender=Post)
def delete_post(sender, instance, **kwargs):
    cache_key = 'post-list'
    cache.delete(cache_key)
