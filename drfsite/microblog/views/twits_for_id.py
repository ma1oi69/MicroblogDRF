from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from microblog.models.twits import Twits
from microblog.serializers.tweets import TweetsSerializer
from drf_spectacular.utils import extend_schema_view, extend_schema

from django.shortcuts import get_object_or_404
from microblog.permissions.TwitsCreatorOrAdmin import IsAdminOrCreatorTwits
from rest_framework.permissions import IsAdminUser


@extend_schema_view(
    create=extend_schema(
        summary="Получить пост по id",
        responses={
            201: {'description': 'Comment created successfully'},
            400: {'description': 'Invalid request data'}
        }
    ),
    delete=extend_schema(
        summary="Удаление поста по id",
        responses={
            204: {'description': 'Comment deleted successfully'},
            404: {'description': 'Comment not found'}
        }
    ),
    update=extend_schema(
        summary="Обновление поста по id",
        responses={
            200: {'description': 'Comment updated successfully'},
            400: {'description': 'Invalid request data'},
            404: {'description': 'Comment not found'}
        }
    )
)
class TwitsForIdAPIView(APIView):

    permission_classes = (IsAdminOrCreatorTwits, )

    @extend_schema(
        summary="Получить пост по ID",
        responses={200: TweetsSerializer(many=True),
                   404: "Пост не найден"},
    )
    def get(self, request, pk):
        twit = get_object_or_404(Twits, id=pk)
        serializer = TweetsSerializer(twit)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Удалить пост по ID",
        responses={204: {'description': 'Пост успешно удален'},
                   404: {'description': 'Пост не найден'}},
    )
    def delete(self, request, pk):
        twit = get_object_or_404(Twits, id=pk)
        twit.delete()
        return Response({'message': 'Пост был успешно удален'}, status=status.HTTP_204_NO_CONTENT)

    @extend_schema(
        summary="Обновить пост по ID",
        responses={200: TweetsSerializer(many=True),
                   400: {'description': 'Неверные данные запроса'},
                   404: {'description': 'Пост не найден'}},
    )
    def put(self, request, pk):
        twit = get_object_or_404(Twits, id=pk)
        serializer = TweetsSerializer(twit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
