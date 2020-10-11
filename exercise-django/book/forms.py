from django import forms
from django.forms.widgets import DateInput

from book.models import Book, Publisher, Author


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'image', 'price', 'author', 'publisher']
#

