from rest_framework import serializers
from .models import LazyUser, LazyUserManager

class LazyUserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='user_id', read_only=True)

    class Meta:
        model = LazyUser
        fields = [
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'is_active'
        ]
