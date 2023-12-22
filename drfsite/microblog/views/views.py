from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from microblog.serializers.tweets import TweetsSerializer
from microblog.services.twits import create_twits
from microblog.models.twits import Twits
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from microblog.models.user import CustomUser
from microblog.exceptions import UserNotExists
from microblog.services.twits import create_user


class TwitsAPIView(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    def get(self, request):
        twits = Twits.objects.filter(user_id=request.user.id)
        serializer = TweetsSerializer(twits, many=True).data
        return Response({'twits': serializer})

    def post(self, request):
        user = request.user.id
        serializer = TweetsSerializer(data=request.data)
        if serializer.is_valid():
            create_twits(serializer, user)
            return Response('NICE', status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TwitsIdAPIView(APIView):
    permission_classes = (IsAuthenticated,)

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


class RegisterAPIView(APIView):

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        username = request.data.get('username')
        create_user(email, password, username)
        return Response('NICE', status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        user = CustomUser.objects.get(pk=pk)
        user.delete()
        return Response({'detail': 'User deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
