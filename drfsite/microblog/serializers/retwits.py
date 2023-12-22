from rest_framework import serializers


class RetwitsSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    tweets_id = serializers.IntegerField()
    created_at = serializers.DateTimeField(read_only=True)
