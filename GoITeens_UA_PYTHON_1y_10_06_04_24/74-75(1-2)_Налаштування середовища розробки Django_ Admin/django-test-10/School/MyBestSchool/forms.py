from django import forms

from .models import Cabinet, Subject


class CabinetForm(forms.Form):
    name = forms.CharField(
        max_length=20,
        label="Назва кабінету",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )


class SubjectForm(forms.Form):
    name = forms.CharField(
        max_length=20,
        label="Назва предмету",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )


class StudentForm(forms.Form):
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
    bio = forms.CharField(
        label="Біографія",
        widget=forms.Textarea(attrs={"class": "form-control"})
    )
    age = forms.IntegerField(
        min_value=6,
        max_value=20,
        label="Ваш вік",
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    cabinet = forms.ModelChoiceField(
        queryset=Cabinet.objects.all(),
        label="Виберіть кабінет",
        widget=forms.Select(attrs={"class": "form-select"})
    )
    subjects = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        label="Виберіть шкільні предмети",
        widget=forms.SelectMultiple(attrs={"class": "form-select"})
    )
