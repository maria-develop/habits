import requests

from config import settings


def send_habit_tg(chat_id, message):
    """
        Отправка сообщения в телеграм чат
        :param chat_id: id чата
        :param message: текст сообщения
        return:
        """
    params = {
        "chat_id": chat_id,
        "text": message
    }
    requests.get(f'{settings.TELEGRAM_BOT_URL}{settings.TELEGRAM_BOT_TOKEN}/sendMessage', params=params)
