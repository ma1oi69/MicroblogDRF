from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from microblog.models.twits import Twits
from microblog.serializers.tweets import TweetsSerializer, CreateTweetsSerializer
from microblog.services.twits import create_twits

from rest_framework.permissions import IsAuthenticated


@extend_schema_view(
    list=extend_schema(
        summary="Получить список постов",
    ),
    create=extend_schema(
        summary="Создание нового поста",
    ),
)
class TwitsAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    @extend_schema(
        summary="Получить список постов этого юзера",
        responses={200: TweetsSerializer(many=True)},
    )
    def get(self, request):
        """
        Получить список постов.
        """
        tweets = Twits.objects.order_by('-created_at')
        serializer = TweetsSerializer(tweets, many=True)
        return Response({'twits': serializer.data})

    @extend_schema(
        summary="Создание нового поста",
        request=CreateTweetsSerializer,
        responses={
            201: {'description': 'Twit created successfully'},
            400: {'description': 'Invalid request data'}
        }
    )
    def post(self, request):
        """
        Создание нового поста.
        """
        user = request.user.id
        serializer = CreateTweetsSerializer(data=request.data)
        if serializer.is_valid():
            create_twits(serializer, user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
