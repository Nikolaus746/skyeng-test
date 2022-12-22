import django_filters
from .models import Note


class NoteFilter(django_filters.FilterSet):

    datetime__gt = django_filters.DateFilter(field_name='datetime', lookup_expr='date__gte')
    datetime__lt = django_filters.DateFilter(field_name='datetime', lookup_expr='date__lte')

    title = django_filters.CharFilter(lookup_expr='icontains', field_name='title')
    is_favorites = django_filters.BooleanFilter(field_name='is_favorites')

    class Meta:
        model = Note
        fields = ['title', 'is_favorites']

