from django import forms
from .models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
        labels = {
            "name": "Author Name",
            "biography": "Biography",
        }
        help_texts = {
            "name": "Enter the full name of the author.",
            "biography": "You can leave this empty if you do not want to add a biography.",
        }
        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Enter author name",
            }),
            "biography": forms.Textarea(attrs={
                "placeholder": "Enter short biography",
                "rows": 5,
            }),
        }

    def clean_name(self):
        name = self.cleaned_data["name"]

        if len(name) < 3:
            raise forms.ValidationError("Author name must be at least 3 characters long.")

        return name