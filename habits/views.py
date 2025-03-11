from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import AllowAny

from users.permissions import IsOwner

from .models import Habit
from .paginations import CustomPageNumberPagination
from .serializers import HabitSerializer


class HabitCreateAPIView(CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitListAPIView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsOwner,)
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        queryset = self.queryset.filter(owner=self.request.user)
        return queryset


class HabitRetrieveAPIView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsOwner,)


class HabitUpdateAPIView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsOwner,)


class HabitDestroyAPIView(DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsOwner,)

    # @receiver(post_delete, sender=Habit)
    # def delete_habit_reminder(sender, instance, **kwargs):
    #     task_name = f"Send Reminder for Habit {instance.id}"
    #     task = PeriodicTask.objects.filter(name=task_name)
    #     if task.exists():
    #         task.delete()


class PublicHabitsListView(ListAPIView):
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    permission_classes = [AllowAny]
    pagination_class = CustomPageNumberPagination
