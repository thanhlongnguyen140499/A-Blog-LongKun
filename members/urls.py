from re import template
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('edit-profile/<int:pk>/', views.UserEditView.as_view(), name='edit-profile'),
    path('edit-profile/password/', views.UserChangePasswordView.as_view(), name='change-password'),
    path('password-success/', views.PasswordSuccessView, name='success-password'),
    path('<int:pk>/profile/', views.ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page/profile/', views.EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', views.CreateProfilePageView.as_view(), name='create_profile_page'),
]