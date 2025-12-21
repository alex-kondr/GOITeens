from django import forms

from .models import Subscription


class SubscriptionForm(forms.Form):
    subscription = forms.ModelChoiceField(
        queryset=Subscription.objects.all(),
        empty_label="Виберіть свою підписку",
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True
    )
