from django.conf import settings
from django.db import models


class Habit(models.Model):
    PERIOD_CHOICES = [
        (1, 'Ежедневно'),
        (7, 'Еженедельно'),
    ]

    name = models.CharField(
        max_length=255,
        verbose_name="Название привычки",
        help_text="Укажите название привычки",
    )
    action = models.TextField(
        blank=True,
        null=True,
        verbose_name="Действие",
        help_text="Укажите, что нужно сделать",
    )
    place = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Место",
        help_text="Укажите, где нужно сделать действие",
    )
    time = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name="Время",
        help_text="Укажите время для действия, например, 08:00 ч",
    )
    is_pleasant = models.BooleanField(
        default=False,
        blank=True,
        null=True,
        verbose_name="Приятная привычка",
        help_text="Укажите, это приятная привычка?",
    )
    related_habit = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Связанная привычка",
        help_text="Укажите полезную связанную привычку",
        limit_choices_to={'is_pleasant': True}
    )
    periodicity = models.PositiveSmallIntegerField(
        choices=PERIOD_CHOICES,
        default=1,
        blank=True,
        null=True,
        verbose_name="Периодичность",
        help_text="1 - ежедневно, 7 - еженедельно",
    )
    reward = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Вознаграждение",
        help_text="Укажите вознаграждение за выполнение полезной привычки",
    )
    estimated_time = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        verbose_name="Время на выполнение (секунды)",
        help_text="Укажите время выполнения полезной привычки",
        default=120
    )
    is_public = models.BooleanField(
        blank=True,
        null=True,
        default=False,
        verbose_name="Публичная привычка",
        help_text="Укажите публичность привычки",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Владелец привычки",
        help_text="Укажите владельца привычки",
    )

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
