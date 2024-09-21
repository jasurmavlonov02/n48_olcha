from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from olcha import views

urlpatterns = [
    path('categories/', views.CategoryListApiView.as_view(), name='categories')

]
