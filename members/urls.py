from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('edit-profile/<int:pk>/', views.UserEditView.as_view(), name='edit-profile'),
]