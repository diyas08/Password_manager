from rest_framework import serializers
from .models import PasswordModel


class PasswordGeneratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordModel
        fields = '__all__'
