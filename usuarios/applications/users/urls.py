from django import urls
from django.urls import path

from . import views

app_name="users_app" #este es el nombre que tendrá este conjunto de urls

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user-register'),
    path('login/', views.LoginUser.as_view(), name='user-login'),
    path('logout/', views.LogoutView.as_view(), name='user-logout'),
    path('update/', views.UpdatePasswordView.as_view(), name='user-update'),
    path('user-verification/<pk>/',views.CodeVerificationView.as_view(), name='user-verification'),
]