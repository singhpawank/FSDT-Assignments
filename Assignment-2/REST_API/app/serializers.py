from rest_framework import serializers
from .models import User, Event

# For adding new user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# For listing users
class UserViewSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    def get_gender(self, obj):
        return obj.get_gender_display()

# For new event
class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'

# For listing events
class EventViewSerializer(serializers.ModelSerializer):
    occurance = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'

    def get_occurance(self, obj):
        return obj.get_occurance_display()
