from django.contrib import admin
from .models import Note

# Admin for Note
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'user',
                    'date', 'category', 'is_favorites', "is_published")
    list_display_links = ('title', )
    empty_value_display = '-empty-'
    date_hierarchy = 'date'
    fields = (('title', 'text',), "category", "is_favorites", "is_published", "user")



admin.site.register(Note, NoteAdmin)
