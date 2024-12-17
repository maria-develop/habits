# Generated by Django 5.1.4 on 2024-12-16 04:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0004_habit_telegram_chat_id_alter_habit_is_pleasant_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='update_habit',
            field=models.ManyToManyField(blank=True, help_text='Укажите обновление привычки', null=True, related_name='habit_update', to=settings.AUTH_USER_MODEL, verbose_name='Обновление привычки'),
        ),
    ]
