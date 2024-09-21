from django.urls import path

from book.views import BookListApiView, BookCreateApiView, BookDetailApiView, BookUpdateApiView, BookDeleteApiView,CreateCategory

urlpatterns = [

    path('all/books/', BookListApiView.as_view(), name='index'),
    path('create/book/', BookCreateApiView.as_view(), name='create_book'),
    path('all/books/<int:pk>/', BookDetailApiView.as_view(), name='detail'),
    path('update/book/<int:pk>/', BookUpdateApiView.as_view(), name='update'),
    path('delete/book/<int:pk>/', BookDeleteApiView.as_view(), name='delete'),

    path('categories/',CreateCategory.as_view(), name='categories')
]
