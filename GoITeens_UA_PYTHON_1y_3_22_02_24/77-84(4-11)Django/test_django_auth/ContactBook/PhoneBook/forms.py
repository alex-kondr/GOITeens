from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class": "form-control text-center"}), label="Ім'я")
    last_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class": "form-control text-center"}), label="Прізвище")
    phone_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class": "form-control text-center"}), label="Номер телефону")
    email = forms.EmailField(max_length=20, required=False, widget=forms.EmailInput(attrs={"class": "form-control text-center"}), label="Електронна адреса")
    address = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={"class": "form-control text-center"}), label="Адреса")
    profile_picture = forms.ImageField(required=False, widget=forms.FileInput(attrs={"class": "form-control text-center"}), label="Фотографія профіля")

    class Meta:
        model = Contact
        fields = ("first_name", "last_name", "phone_number", "email", "address", "profile_picture")
