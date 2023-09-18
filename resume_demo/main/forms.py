from django import forms
from .models import ContactProfile


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "*Full.."}),
    )
    email = forms.CharField(
        max_length=254,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "*Email.."}),
    )

    message = forms.CharField(
        max_length=254,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "*Your Message..", "rows": 6}),
    )

    class Meta:
        model = ContactProfile
        fields = (
            "name",
            "email",
            "message",
        )
