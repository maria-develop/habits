from django.urls import path

from .apps import HabitsConfig
from .views import (HabitCreateAPIView, HabitDestroyAPIView, HabitListAPIView,
                    HabitRetrieveAPIView, HabitUpdateAPIView,
                    PublicHabitsListView)

app_name = HabitsConfig.name


urlpatterns = [
    path("", HabitListAPIView.as_view(), name="habit_list"),
    path("<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit_retrieve"),
    path("create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path(
        "<int:pk>/delete/",
        HabitDestroyAPIView.as_view(),
        name="habit_delete",
    ),
    path(
        "<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habit_update"
    ),
    path('public/', PublicHabitsListView.as_view(), name='public-habits'),
]
