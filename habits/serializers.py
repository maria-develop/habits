from rest_framework import serializers
from .models import Habit
from .validators import HabitsValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [HabitsValidator]
        # read_only_fields = ('user',)
