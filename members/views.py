from django.db.models.query_utils import subclasses
from django.urls.base import reverse_lazy
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic.edit import UpdateView
from .forms import PasswordChangingForm, SignUpForm, EditProfileForm

# Create your views here.
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


