from django.forms import ModelForm
from .models import Note
from django import forms


class NoteModelForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text',
                  'category', 'is_favorites', 'is_published']

