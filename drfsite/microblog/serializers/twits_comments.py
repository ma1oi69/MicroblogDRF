from rest_framework import serializers


class TwitsCommentSerializer(serializers.Serializer):
    tweets_id = serializers.IntegerField()
    comments = serializers.IntegerField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
