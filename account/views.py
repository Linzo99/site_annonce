from django.shortcuts import render, redirect
from django.views.generic import FormView, View
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from .models import Profile
from .forms import LoginForm, UserRegistrationForm

# Create your views here.

# inherit from LoginView and LogoutView from django
class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    redirect_authenticated_user = True
    
class CustomLogoutView(LogoutView):
    pass


class RegisterView(CreateView):
    form_class = UserRegistrationForm
    success_url = '/account/login/'
    template_name = 'account/register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        Profile.objects.create(user=user)
        messages.success(self.request, 'Account successfully createt')
        return super().form_valid(form)

