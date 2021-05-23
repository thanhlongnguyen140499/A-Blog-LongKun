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
        fields = ('title', 'title_tag', 'author', 'category' ,'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is title ...'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list,attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        # fields = '__all__'
    
    def clean_name(self):
            """
            ensure that name is always lower case.
            """
            return self.cleaned_data['name'].lower()

    widget = {
        'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-transform:lowercase;'})
    }

    
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