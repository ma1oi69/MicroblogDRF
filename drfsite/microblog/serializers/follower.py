from rest_framework import serializers


class FollowersSerializer(serializers.Serializer):
    followers = serializers.IntegerField()
    subscriptions = serializers.IntegerField()