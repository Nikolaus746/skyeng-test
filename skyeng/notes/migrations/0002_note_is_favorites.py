# Generated by Django 4.1.4 on 2022-12-21 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='is_favorites',
            field=models.BooleanField(default=False, verbose_name='Избранное'),
        ),
    ]
