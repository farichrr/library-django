from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'author',
            'publication',
            'title',
            'price',
            'isbn',
        ]
        labels = {
            'author':'Author    ',
            'publication':'Pub Date',
            'title':'Book Title',
            'price':'Price',
            'isbn':'ISBN',
        }