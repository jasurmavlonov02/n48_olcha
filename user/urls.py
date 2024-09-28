from django.urls import path
from user.views import UserLoginApiView, UserLogoutApiView

urlpatterns = [
    path('get-token/', UserLoginApiView.as_view()),
    path('token-delete/', UserLogoutApiView.as_view())
]
