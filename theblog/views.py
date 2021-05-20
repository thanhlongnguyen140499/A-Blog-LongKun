from django.views.generic.base import View
from theblog.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .forms import PostForm

# Create your views here.
# def home(request):
#     return render(request, 'theblog/home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'theblog/home.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'theblog/article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'theblog/add_post.html'
    # fields = '__all__'   # add all field into CreateView
    # fields = ('title', 'title_tag', 'body', 'author')   # as same as above line
