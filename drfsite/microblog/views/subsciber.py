from rest_framework.views import APIView
from microblog.serializers.follower import FollowersSerializer
from rest_framework.response import Response
from rest_framework import status


class SubscribeAPIView(APIView):
    def post(self, request):
        serializer = FollowersSerializer(data=request.data)
        if serializer.is_valid():

            follower = serializer.create()

            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


