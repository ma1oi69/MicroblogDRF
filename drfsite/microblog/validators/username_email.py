from rest_framework import status
from rest_framework.response import Response

from microblog.models.user import CustomUser
from django.core.exceptions import ObjectDoesNotExist


def validators_username_email(username, email):
    try:
        if CustomUser.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        if CustomUser.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists.'}, status=status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist:
        pass
