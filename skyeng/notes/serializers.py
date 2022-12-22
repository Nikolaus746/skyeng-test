from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ['uuid', 'title', 'text', 'category', 'is_favorites', 'is_published']
