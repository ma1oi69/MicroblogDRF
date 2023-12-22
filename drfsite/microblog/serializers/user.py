from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    sex = serializers.CharField()
    avatar = serializers
    country = serializers.CharField()
    age = serializers.IntegerField()
    date_of_birthday = serializers.DateTimeField()
    about = serializers.CharField(max_length=150)
    