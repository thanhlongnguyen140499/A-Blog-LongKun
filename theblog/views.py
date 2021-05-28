from django.urls.base import reverse_lazy, reverse
from django.views.generic.base import View
from theblog import models
from theblog.models import Comment, Post, Category
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CommentForm, EditForm, PostForm, CategoryForm
from django.http import HttpResponseRedirect

# Create your views here.
# def home(request):
#     return render(request, 'theblog/home.html', {})

def LikeView(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'theblog/home.html'
    # ordering = ['-id'] # to sort arcoding by id 
    ordering = ['-post_date']

    def get_context_data(self, **kwargs):
        categories = Category.objects.all()
        context = super(HomeView, self).get_context_data(**kwargs)
        context['categories'] = categories
        return context
    

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'theblog/article_details.html'

    def get_context_data(self, **kwargs):
        categories = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['categories'] = categories

        stuff = get_object_or_404(Post, id = self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['liked'] = liked

        context['total_likes'] = total_likes
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'theblog/add_post.html'
    # fields = '__all__'   # add all field into CreateView
    # fields = ('title', 'title_tag', 'body', 'author')   # as same as above line


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'theblog/add_comment.html'

    def form_valid(self, form):   # ex: bill create comment -> self : bill
        form.instance.post_id = self.kwargs['pk'] 
        return super().form_valid(form) 
    
    def get_success_url(self):
        return reverse_lazy('article-detail',  kwargs={'pk': self.kwargs['pk']})

class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'theblog/add_category.html'


def CategoryView(request, cats):
    category_list = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'theblog/category.html', {'cats':cats.title().replace('-', ' '), 'category_list':category_list})


def CategoryListView(request):
    category_menu_list = Category.objects.all()
    return render(request, 'theblog/category_list.html', {'categories': category_menu_list})

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm  # if use form_class u must remove fields = (...)
    template_name = 'theblog/update_post.html'
    # fields = ('title', 'title_tag', 'author', 'body')


class DeletePostView(DeleteView):
    model = Post
    template_name = 'theblog/delete_post.html'
    success_url = reverse_lazy('home')