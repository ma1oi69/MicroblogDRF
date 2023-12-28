from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from microblog.models import CustomUser
from microblog.services.twits import create_user
from microblog.validators.username_email import validators_username_email


class RegisterAPIView(APIView):

    def post(self, request):

        email = request.data.get('email')
        password = request.data.get('password')
        username = request.data.get('username')

        validation_response = validators_username_email(username=username, email=email)
        if validation_response is not None:
            return validation_response

        create_user(email, password, username)
        return Response('NICE', status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        try:
            user = CustomUser.objects.get(pk=pk)
            user.delete()
            return Response({'detail': 'User deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)