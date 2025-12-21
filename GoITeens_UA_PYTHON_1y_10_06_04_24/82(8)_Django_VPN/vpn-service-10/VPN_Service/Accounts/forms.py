from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile


class SignUp(UserCreationForm):
    username = forms.CharField(label="Нікнейм", widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label="Підтвердження пароля", widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]



class SignIn(AuthenticationForm):
    username = forms.CharField(label="Нікнейм", widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-control"}))


class UserEdit(forms.ModelForm):
    email = forms.CharField(label="Email", widget=forms.TextInput(attrs={"class": "form-control"}), required=False)

    class Meta:
        model = User
        fields = ["email"]


class ProfileForm(forms.ModelForm):
    phone_number = forms.CharField(label="Номер телефону", widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    bio = forms.CharField(label="Інформація про себе", widget=forms.Textarea(attrs={"class": "form-control"}), required=False)
    avatar = forms.ImageField(label="Фото", widget=forms.FileInput(attrs={"class": "form-control"}), required=False)

    class Meta:
        model = Profile
        exclude = ["user"]
