from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "action", "place", "time", "is_pleasant", "related_habit",
                    "periodicity", "reward", "estimated_time", "is_public", "owner")
    list_filter = ("id", "name", "action", "place", "time", "is_pleasant", "related_habit",
                   "periodicity", "reward", "estimated_time", "is_public", "owner")
