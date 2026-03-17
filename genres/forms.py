from django import forms
from .models import Genre


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = "__all__"
        labels = {
            "name": "Genre Name",
            "description": "Description",
        }
        help_texts = {
            "name": "Enter the name of the genre.",
            "description": "Optional short description of the genre.",
        }
        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Enter genre name",
            }),
            "description": forms.Textarea(attrs={
                "placeholder": "Enter genre description",
                "rows": 4,
            }),
        }