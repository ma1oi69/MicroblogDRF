from rest_framework import serializers


class CommentsSerializer(serializers.Serializer):
    tweet_id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    like = serializers.IntegerField(default=0)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

