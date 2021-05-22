from django import urls
from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('add-post/', views.AddPostView.as_view(), name='add-post'),
    path('article/edit/<int:pk>/', views.UpdatePostView.as_view(), name='update-post'),
    path('article/<int:pk>/remove/', views.DeletePostView.as_view(), name='delete-post'),
    path('add_category/', views.AddCategoryView.as_view(), name='add-category'),
    path('categories/<str:cats>/', views.CategoryView, name='category'),
    path('category-list/', views.CategoryListView, name='category-list'),
    path('like/<int:pk>/', views.LikeView , name='like-post'),
]
