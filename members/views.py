from django.urls.base import reverse_lazy
from django.db import models
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic.edit import UpdateView
from .forms import SignUpForm, EditProfileForm
# Create your views here.
class UserRegisterView(CreateView):
    # form_class = UserCreationForm
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user