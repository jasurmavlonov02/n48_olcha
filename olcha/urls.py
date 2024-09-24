from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from olcha.views import category,group,product


urlpatterns = [
    path('categories/', category.CategoryListApiView.as_view(), name='categories'),
    path('groups/', group.GroupListApiView.as_view(), name='groups'),
    path('category/<slug:slug>/',category.CategoryDetailApiView.as_view(), name='category'),
    path('all-products/', product.ProductListApiView.as_view(),name='all-products'),
    path('all-images/', product.ImageListApiView.as_view(),name='all-products'),

]
