from django import forms
from .models import Book
from django.core.exceptions import ValidationError

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'publication_date', 'pages']

    def clean_author(self):
        author = self.cleaned_data.get('author')
        if author.startswith(' ') or author.endswith(' '):
            raise ValidationError("Author cannot start or end with a space")
        if '~' in author:
            raise ValidationError("Author cannot contain the '~' character")
        return author.strip()

    def clean_publisher(self):
        publisher = self.cleaned_data.get('publisher')
        if publisher.startswith(' ') or publisher.endswith(' '):
            raise ValidationError("Publisher cannot start or end with a space")
        if '~' in publisher:
            raise ValidationError("Publisher cannot contain the '~' character")
        return publisher.strip()