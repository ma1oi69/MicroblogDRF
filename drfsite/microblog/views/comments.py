from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from microblog.exceptions import TwitsNotExists
from microblog.models import Comments
from microblog.models.twits import Twits
from microblog.serializers.comments import CommentsSerializer
from microblog.services.twits import create_comment


class CommentsAPIView(APIView):

    def post(self, request):

        title = request.data.get('title')
        tweet_id = request.data.get('tweet_id')

        try:
            tweet = Twits.objects.get(id=tweet_id)

        except TwitsNotExists:
            return Response({"detail": "Tweet does not exist."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CommentsSerializer(data=request.data)

        if serializer.is_valid():
            create_comment(title, tweet_id)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        comment = Comments.objects.get(id=pk)
        comment.delete()

        return Response({'detail': 'Comment deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):

        comment = Comments.objects.get(id=pk)
        serializer = CommentsSerializer(comment, data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)