from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        labels = {
            "title": "Book Title",
            "description": "Description",
            "author": "Author",
            "genres": "Genres",
        }
        help_texts = {
            "title": "Enter the title of the book.",
            "description": "Write a short description of the book.",
            "author": "Choose an existing author.",
            "genres": "Choose one or more genres.",
        }
        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Enter book title",
            }),
            "description": forms.Textarea(attrs={
                "placeholder": "Enter book description",
                "rows": 5,
            }),
        }