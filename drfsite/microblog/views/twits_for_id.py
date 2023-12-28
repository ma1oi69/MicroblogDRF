from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from microblog.models.twits import Twits
from microblog.serializers.tweets import TweetsSerializer


class TwitsForIdAPIView(APIView):

    def get(self, request, pk):
        try:
            twit = Twits.objects.get(id=pk)
            serializer = TweetsSerializer(twit)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            twit = Twits.objects.get(id=pk)
            twit.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        twit = Twits.objects.get(id=pk)
        serializer = TweetsSerializer(twit, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)