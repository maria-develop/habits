# Generated by Django 5.1.4 on 2024-12-17 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0006_remove_habit_telegram_chat_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='update_habit',
        ),
    ]
