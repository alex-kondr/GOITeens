from django import forms

from .models import Planer
from PhoneBook.models import Contact


class PlanerForm(forms.ModelForm):
    contact = forms.ModelChoiceField(
        label="Контакт",
        widget=forms.Select(attrs={"class": "form-select"}),
        queryset=Contact.objects.all()
    )
    title = forms.CharField(
        label="Тема зустрічі",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    description = forms.CharField(
        label="Додаткова інформаці (необов'язково)",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=False
    )
    date = forms.DateTimeField(
        label="Дата та час зустрічі у форматі '2025-10-26T10:30'",
        input_formats=["%Y-%m-%dT%H:%M", "%d-%m-%YT%H:%M"],
        widget=forms.DateTimeInput(attrs={
            "class": "form-control",
            "type": "datetime-local"
        })
    )
    url = forms.URLField(
        label="Посилання для онлайн-зустрічі (необов'язково)",
        widget=forms.URLInput(attrs={"class": "form-control"}),
        required=False
    )
    place = forms.CharField(
        label="Місце зустрічі",
        initial="Online",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Planer
        exclude = ["user", "accept"]
