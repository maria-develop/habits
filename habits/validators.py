from rest_framework import serializers


class HabitsValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value['is_pleasant']:
            if value['related_habit'] or value['reward']:
                raise serializers.ValidationError(
                    'У приятной привычки не может быть связанной привычки или вознаграждения')
            if value['related_habit'] and value['reward']:
                raise serializers.ValidationError(
                    'Может быть связанная привычка или вознаграждение,')
            if value['estimated_time'] > 120:
                raise serializers.ValidationError(
                    'Длительность привычки не может быть больше 120 секунд')
            if value['related_habit']:
                if not value['related_habit'].is_pleasant:
                    raise serializers.ValidationError('Связанные привычки = приятные привычки')
