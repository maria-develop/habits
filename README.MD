# Описание проекта

Этот проект посвящен приобретению новых полезных привычек и искоренению старых плохих привычек.
Реалезован функционал с отправкой в телеграм

Проект реализует:

CRUD-операции для привычек через API.
Связь между привычками и пользователями.
Настроены права доступа к функционалу по владельцу привычки.
Настроена пагинация.
Настроена асинхронная рассылка в телеграм пользователям о привычках с помощью Celery.
Написаны тесты.

## Функциональные возможности

1. Кастомная модель пользователя:
Аутентификация через email.
Поля: телефон, id телеграм

2. Управление привычками:
CRUD-операции для привычек (создание, получение списка, обновление, удаление).
Реализовано с использованием APIView.


## Установка

1. Клонируйте репозиторий:
https://github.com/maria-develop/habits

2. Создайте виртуальное окружение и активируйте его:
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows

3. Установите зависимости:
pip install -r requirements.txt

4. Примените миграции:
python manage.py migrate

5. Запустите сервер:
python manage.py runserver


## Использование API


Привычка (/habits/):

GET /habits/ — Получение списка привычек.

POST /habits/ — Создание нового привычек.

GET /habits/{id}/ — Получение информации об привычке.

PUT /habits/{id}/update/ — Полное обновление привычки.

PATCH /habits/{id}/update/ — Частичное обновление привычки.

DELETE /habits/{id}/delete/ — Удаление привычки.


## Проверка API
Рекомендуется использовать Postman или другой инструмент для тестирования API.
Примеры запросов:

Создание курса:

POST /courses/
{
    "name": "Python Basics",
    "description": "Курс по основам Python"
}

Создание привычки:

POST /habits/
{
    "name": "бег",
    "action": "бегать",
    "place": "на улице",
    "time": "12-00",
}

Создание пользователя:

POST /users/
{
    "email": "us@mail.ru",
    "phone": "+123456789",
    "telegram_chat_id": "1324564"
}


## Тесты
Реализованы тесты для функционала привычек.