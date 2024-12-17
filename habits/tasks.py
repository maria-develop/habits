from datetime import datetime

from celery import shared_task

from habits.models import Habit
from habits.services import send_habit_tg


@shared_task
def send_habit_reminder():
    habits = Habit.objects.all()
    now = datetime.now()
    current_date = now.strftime('%H:%M')
    for habit in habits:
        if habit.time >= current_date:
            user = habit.owner
            tg_chat = user.telegram_chat_id
            message = f"Я буду {habit.action} в {habit.time} в {habit.place}."
            send_habit_tg(tg_chat, message)  # Отправляем привычку в Telegram чат
