from rest_framework import serializers


class UserProfileSerializer(serializers.Serializer):
    username = serializers.CharField()
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    country = serializers.CharField()
    about = serializers.CharField()
