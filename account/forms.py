from django import forms
from .models import Profile
from django.contrib.auth import get_user_model

# this is not used 
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput())
    confirm = forms.CharField(label='confirm', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'email')

    def clean_confirm(self):
        cd = self.cleaned_data
        if cd['password'] != cd['confirm']:
            raise forms.ValidationError("Passwords don't match")

        return cd['confirm']


class UserEditForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')

    
class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')