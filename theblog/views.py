from django.urls.base import reverse_lazy
from django.views.generic.base import View
from theblog import models
from theblog.models import Post, Category
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import EditForm, PostForm, CategoryForm

# Create your views here.
# def home(request):
#     return render(request, 'theblog/home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'theblog/home.html'
    # ordering = ['-id'] # to sort arcoding by id 
    ordering = ['-post_date']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'theblog/article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'theblog/add_post.html'
    # fields = '__all__'   # add all field into CreateView
    # fields = ('title', 'title_tag', 'body', 'author')   # as same as above line

class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'theblog/add_category.html'

def CategoryView(request, cats):
    category_list = Post.objects.filter(category=cats)
    return render(request, 'theblog/category.html', {'cats':cats.title(), 'category_list':category_list})


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm  # if use form_class u must remove fields = (...)
    template_name = 'theblog/update_post.html'
    # fields = ('title', 'title_tag', 'author', 'body')


class DeletePostView(DeleteView):
    model = Post
    template_name = 'theblog/delete_post.html'
    success_url = reverse_lazy('home')