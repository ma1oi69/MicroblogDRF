from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from microblog.models import Comments
from microblog.models.twits import Twits
from microblog.serializers.comments import CommentsSerializer, CreateCommentsSerializer, UpdateCommentsSerializer
from microblog.services.twits import create_comment


from drf_spectacular.utils import extend_schema_view, extend_schema


@extend_schema_view(
    create=extend_schema(
        summary="Создание комментария для поста",
        request=CommentsSerializer,
        responses={
            201: {'description': 'Comment created successfully'},
            400: {'description': 'Invalid request data'}
        }
    ),
    delete=extend_schema(
        summary="Удаление комментария по идентификатору",
        responses={
            204: {'description': 'Comment deleted successfully'},
            404: {'description': 'Comment not found'}
        }
    ),
    update=extend_schema(
        summary="Обновление комментария по идентификатору",
        responses={
            200: {'description': 'Comment updated successfully'},
            400: {'description': 'Invalid request data'},
            404: {'description': 'Comment not found'}
        }
    )
)
class CreateCommentsAPIView(APIView):
    """
    Описание представления CreateCommentsAPIView.
    """

    @extend_schema(
        summary="Получение комментариев для поста",
        responses={
            200: CommentsSerializer(many=True)
        }
    )
    def get(self, request, tweet_id):
        """
        Получение комментариев для поста.
        """
        comments = Comments.objects.filter(tweet_id=tweet_id).order_by('-created_at')
        serializer = CommentsSerializer(comments, many=True)
        return Response({'comments': serializer.data})

    @extend_schema(
        summary="Создание комментария для поста",
        request=CreateCommentsSerializer,
        responses={
            201: {'description': 'Comment created successfully'},
            400: {'description': 'Invalid request data'},
            404: {'description': 'Tweet not found'}
        }
    )
    def post(self, request, tweet_id):
        """
        Создание комментария для поста.
        """
        title = request.data.get('title')
        tweet = None

        try:
            tweet = Twits.objects.get(id=tweet_id)
        except Twits.DoesNotExist:
            return Response({"detail": "Tweet does not exist."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CreateCommentsSerializer(data=request.data)

        if serializer.is_valid():
            create_comment(title, tweet_id)
            tweet.answers += 1
            tweet.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteCommentAPIView(APIView):
    """
    Описание представления DeleteCommentAPIView.
    """

    @extend_schema(
        summary="Удаление комментария по идентификатору",
        responses={
            204: {'description': 'Comment deleted successfully'},
            404: {'description': 'Comment not found'}
        }
    )
    def delete(self, request, pk):
        """
        Удаление комментария по идентификатору.
        """
        try:
            comment = Comments.objects.get(id=pk)
            comment.delete()
            return Response({'detail': 'Comment deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except Comments.DoesNotExist:
            return Response({'detail': 'Comment not found.'}, status=status.HTTP_404_NOT_FOUND)


class UpdateCommentAPIView(APIView):
    """
    Описание представления UpdateCommentAPIView.
    """

    @extend_schema(
        request=UpdateCommentsSerializer,
        summary="Апдейт комментария по идентификатору",
        responses={
            200: {'description': 'Comment updated successfully'},
            400: {'description': 'Invalid request data'},
            404: {'description': 'Comment not found'}
        }
    )
    def patch(self, request, pk):
        """
        Апдейт комментария по идентификатору.
        """
        try:
            comment = Comments.objects.get(id=pk)
        except Comments.DoesNotExist:
            return Response({'detail': 'Comment not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CommentsSerializer(comment, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

