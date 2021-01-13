from rest_framework import serializers  #, validators

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User
