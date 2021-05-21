from django.urls.base import reverse_lazy
from django.db import models
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
