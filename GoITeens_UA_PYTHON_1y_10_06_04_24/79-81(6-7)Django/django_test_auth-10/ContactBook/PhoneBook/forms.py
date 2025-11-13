from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=20,
        label="Ім'я",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        max_length=20,
        label="Прізвище",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    phone_number = forms.CharField(
        max_length=16,
        label="Номер телефону",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        max_length=200,
        label="Електронна адреса",
        widget=forms.EmailInput(attrs={"class": "form-control"}),
        required=False
    )
    address = forms.CharField(
        max_length=200,
        label="Адреса",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=False
    )
    bio = forms.CharField(
        label="Інформація про контакт",
        widget=forms.Textarea(attrs={"class": "form-control"}),
        required=False
    )
    age = forms.IntegerField(
        label="Вік",
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        required=False
    )
    profile_picture = forms.ImageField(
        label="Аватарка",
        widget=forms.FileInput(attrs={"class": "form-control"}),
        required=False
    )

    class Meta:
        model = Contact
        fields = ("first_name", "last_name", "phone_number", "email", "address", "age", "bio", "profile_picture")


class FilterForm(forms.Form):
    first_name = forms.CharField(
        max_length=20,
        label="Ім'я",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=False
    )
    last_name = forms.CharField(
        max_length=20,
        label="Прізвище",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=False
    )
    phone_number = forms.CharField(
        max_length=16,
        label="Номер телефону",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=False
    )
    email = forms.EmailField(
        max_length=200,
        label="Електронна адреса",
        widget=forms.EmailInput(attrs={"class": "form-control"}),
        required=False
    )
    address = forms.CharField(
        max_length=200,
        label="Адреса",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=False
    )
