from django import forms

from genres.models import Genre


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ["name", "description"]