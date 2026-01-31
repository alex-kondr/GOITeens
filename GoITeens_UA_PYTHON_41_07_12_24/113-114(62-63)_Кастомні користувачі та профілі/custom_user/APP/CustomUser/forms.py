from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Profile


class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "email", "bio", "phone_number", "place", "password1", "password2"]


class UpdateUserForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "bio", "phone_number", "place"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["user"]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)
