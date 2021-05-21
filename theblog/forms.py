from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ('title', 'title_tag', 'author', 'category' ,'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is title ...'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list,attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        # fields = ('title', 'title_tag', 'author', 'category' ,'body')

        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is title ...'}),
        #     'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
        #     'author': forms.Select(attrs={'class': 'form-control'}),
        #     'category': forms.Select(choices=choice_list,attrs={'class': 'form-control'}),
        #     'body': forms.Textarea(attrs={'class': 'form-control'}),
        # }

    
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is title ...'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list,attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }