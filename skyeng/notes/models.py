import uuid
from django.db import models
from django.contrib.auth.models import User

# Class represents notes.
CATEGORY_CHOICES = [
    ('link', 'Ссылка'),
    ('note', 'Заметка'),
    ('memo', 'Памятка'),
    ('todo', 'TODO'),

]

class Note(models.Model):
    title = models.CharField(max_length=200, null=True, verbose_name="Название")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    text = models.TextField(null=True, blank=True, verbose_name="Текст заметки")
    datetime = models.DateTimeField(auto_now_add=True)
    date = models.DateField(auto_now=True, verbose_name="Дата редактирования")
    category = models.CharField(max_length=4, choices=CATEGORY_CHOICES, null=True, blank=True)
    is_favorites = models.BooleanField(default=False, verbose_name="Избранное")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано?")
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"

    def __str__(self):
        return F"{self.title} -- {self.user}"
