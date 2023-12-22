from rest_framework import serializers
from microblog.models.twits import Twits
from datetime import datetime


class TweetsSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=400)
    like = serializers.IntegerField(default=0)
    answers = serializers.IntegerField(default=0)
    repost = serializers.IntegerField(default=0)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance




