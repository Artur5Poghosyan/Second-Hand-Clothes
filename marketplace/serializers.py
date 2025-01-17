from rest_framework import serializers
from .models import User, Garment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'address']

class GarmentSerializer(serializers.ModelSerializer):
    publisher = UserSerializer(read_only=True)

    class Meta:
        model = Garment
        fields = ['id', 'type', 'description', 'publisher', 'size', 'price']
