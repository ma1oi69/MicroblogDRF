from rest_framework import serializers
from microblog.models.user import CustomUser


class SubscriptionSerializer(serializers.ModelSerializer):
    follower = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    following = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
