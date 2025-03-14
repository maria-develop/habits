# Generated by Django 5.1.4 on 2024-12-16 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_alter_habit_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='telegram_chat_id',
            field=models.CharField(blank=True, help_text='Укажите id в телеграм', max_length=100, null=True, verbose_name='Телеграм id'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='is_pleasant',
            field=models.BooleanField(blank=True, default=False, help_text='Укажите, это приятная привычка?', null=True, verbose_name='Приятная привычка'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='periodicity',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Ежедневно'), (7, 'Еженедельно')], default=1, help_text='1 - ежедневно, 7 - еженедельно', null=True, verbose_name='Периодичность'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='time',
            field=models.CharField(blank=True, help_text='Укажите время для действия, например, 08:00 ч', max_length=30, null=True, verbose_name='Время'),
        ),
    ]
