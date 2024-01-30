from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from microblog.models import Follower, CustomUser
from microblog.serializers.follower import SubscriptionSerializer
from microblog.exceptions import UserNotFound


class SubscribeAPIView(APIView):
    def post(self, request):
        user = request.user
        following_id = request.data.get('following_id')

        try:
            following = CustomUser.objects.get(id=following_id)
        except UserNotFound:
            return Response('Пользователь с указанным идентификатором не найден', status=status.HTTP_404_NOT_FOUND)

        subscription = Follower(followers=user)
        subscription.save()
        subscription.subscriptions.set([following])  # Используйте метод set() для установки связи

        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
