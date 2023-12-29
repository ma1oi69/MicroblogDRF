from rest_framework import serializers


class CommentsSerializer(serializers.Serializer):
    tweet_id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    like = serializers.IntegerField(default=0)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def update(self, instance, validated_data):
        """
        Обновление комментария с использованием данных запроса.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance


class CreateCommentsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)


class UpdateCommentsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    tweet_id = serializers.IntegerField()