from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import CreateView, FormView, ListView, View

from post.models import Post

from .forms import (LoginForm, ProfileEditForm, UserEditForm,
                    UserRegistrationForm)
from .models import Profile


# Create your views here.
# Views for the profile
class OwnerMixin(LoginRequiredMixin):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)


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


class ProfileView(OwnerMixin, ListView):
    model = Post
    template_name = 'account/profile/dashboard.html'
    context_object_name = 'posts'
    
    def get_context_data(self):
        context = super().get_context_data()
        context['user'] = self.request.user
        return context

@login_required
def edit_user(req):
    user_form = UserEditForm(instance=req.user)
    profile_form = ProfileEditForm(instance=req.user.profile)

    if req.method == "POST":
        user_form = UserEditForm(instance=req.user,
                                 data=req.POST)
        profile_form = ProfileEditForm(instance=req.user.profile,
                                        data=req.POST,
                                        files=req.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(req, 'Votre profile a ete mis a jour')
        
        else:
            messages.error(req, "Formulaire Invalide")
        
        return redirect('account:profile')

    return render(req, 'account/profile/edit.html',{'user_form':user_form,
                                            'profile_form':profile_form})
