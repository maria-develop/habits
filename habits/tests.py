from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase
from unittest.mock import patch

from habits.models import Habit
from habits.tasks import send_habit_reminder
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="django@mail.ru", password='123')
        self.habit = Habit.objects.create(
            owner=self.user, place="на улице", time="12:00:00", action="бег", estimated_time='60'
        )
        self.client.force_authenticate(user=self.user)

    def test_habits_retrieve(self):
        url = reverse("habits:habit_retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), self.habit.place)

    def test_habits_create(self):
        url = reverse("habits:habit_create")
        data = {
            "name": "хурма6",
            "action": "съесть",
            "place": "на улице",
            "time": "12-00",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habits_update(self):
        url = reverse("habits:habit_update", args=(self.habit.pk,))
        data = {
            "place": "дом",
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.get(pk=self.habit.pk).place, "дом")

    def test_habits_delete(self):
        url = reverse("habits:habit_delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habits_list(self):
        url = reverse(
            "habits:habit_list",
        )
        response = self.client.get(url)
        data = response.status_code
        print(data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
