from dataclasses import field
from rest_framework import serializers
from .models import user, item, booking

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model  = user
        fields = '__all__'

class itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = '__all__'

class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = '__all__'
