from re import template
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('edit-profile/<int:pk>/', views.UserEditView.as_view(), name='edit-profile'),
    path('edit-profile/password/', views.UserChangePasswordView.as_view(), name='change-password'),
    path('password-success/', views.PasswordSuccessView, name='success-password'),
]