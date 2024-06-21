from rest_framework import serializers
from .models import UserProfesional
class UserProfesionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfesional
        fields = ['id', 'username', 'email', 'password']