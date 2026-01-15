from django import forms

from .models import Article, Tag


class ArticleForm(forms.ModelForm):
    description = forms.CharField(
        max_length=500,
        label="Опис",
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    class Meta:
        model = Article
        fields = "__all__"
        widgets = {
            "author": forms.Select(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "text": forms.Textarea(attrs={"class": "form-control"}),
            "tags": forms.SelectMultiple(attrs={"class": "form-control"}),
        }
