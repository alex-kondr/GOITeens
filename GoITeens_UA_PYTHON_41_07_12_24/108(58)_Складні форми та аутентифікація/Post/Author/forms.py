from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(
        max_length=500,
        label="Електронна адреса",
        required=False,
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    first_name = forms.CharField(
        label="Ім'я",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=False
    )
    last_name = forms.CharField(
        label="Прізвище",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=False
    )
    class Meta:
        model = User
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Логін",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
