from django.conf.urls import url
from django.contrib.auth import forms
from django.db.models.query_utils import subclasses
from django.urls.base import reverse_lazy
from django.db import models
from django import forms
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic.edit import UpdateView
from .forms import PasswordChangingForm, SignUpForm, EditProfileForm, CreateUserProfileForm
from theblog.models import Profile

# Create your views here.
class CreateProfilePageView(CreateView):
    model = Profile
    form_class = CreateUserProfileForm
    template_name = 'registration/create_user_profile.html'
    # fields = '__all__'
    # success_url = reverse_lazy('home')

    def form_valid(self, form):   # ex: bill create profile -> self : bill
        form.instance.user = self.request.user  # self.request.user = bill -> create instace.user = bill
        return super().form_valid(form) 
        

class EditProfilePageView(UpdateView):
    model = Profile
    template_name = 'registration/edit_user_profile.html'
    fields = '__all__'
    # fields = ('profile_pic', 'website_url', 'fb_url', 'twitter_url', 'instagram_url', 'pinterest_url')
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user.profile


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id = self.kwargs['pk'])
        context['page_user'] = page_user
        return context
    

def PasswordSuccessView(request):
    return render(request, 'registration/success_password.html', {})


class UserChangePasswordView(PasswordChangeView):
    form_class = PasswordChangingForm
    # form_class = PasswordChangeForm
    template_name='registration/change_password.html'
    # success_url = reverse_lazy('home')
    success_url = reverse_lazy('success-password')


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


