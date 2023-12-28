from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from microblog.models.twits import Twits

from microblog.serializers.comments import CommentsSerializer

from microblog.models.comments import Comments


class TweetCommentsAPIView(APIView):
    def get(self, request, pk):

        tweet = get_object_or_404(Twits, id=pk)
        comments = Comments.objects.filter(tweet=tweet)
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)

