from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label="Ваш логін",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        label="Адреса електронної пошти",
        required=False,
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    password1 = forms.CharField(
        label="Ваш пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        label="Ваш пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class SignInForm(forms.Form):
    username = forms.CharField(
        label="Логін",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )


class ProfileForm(forms.ModelForm):
    phone_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"class": "form-control"})
    )
    avatar = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={"class": "form-control"})
    )
    telegram = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    viber = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    github = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Profile
        exclude  = ["user"]


class UserEditForm(forms.ModelForm):
    username = forms.CharField(
        label="Логін",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        label="Адреса електронної пошти",
        widget=forms.EmailInput(attrs={"class": "form-control"}),
        required=False
    )

    class Meta:
        model = User
        fields = ["username", "email"]
