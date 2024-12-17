from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = ['id', 'email', 'phone', 'telegram_chat_id']
        fields = '__all__'
        # fields = [
        #     "id",
        #     "email",
        #     "password",
        #     "is_superuser",
        #     "is_staff",
        #     "telegram_chat_id",
        # ]
