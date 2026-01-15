from django import forms

from .models import Picture, Project


class PictureForm(forms.ModelForm):
    picture = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Picture
        fields = "__all__"


class ProjectForm(forms.ModelForm):
    github = forms.URLField(
        widget=forms.URLInput(attrs={"class": "form-control"})
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"class": "form-control"})
    )
    dockerhub = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Project
        exclude = ["user", "pictures"]
