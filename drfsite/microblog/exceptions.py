from rest_framework.views import exception_handler
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from rest_framework import status
from rest_framework.response import Response


class UserNotExists(Exception):
    ...


class TwitsNotExists(Exception):
    ...


class UserNotFound(Exception):
    ...


class TwitsNotFound(Exception):
    ...


# def custom_exception_handler(exc, context):
#     response = exception_handler(exc, context)
#
#     if isinstance(exc, AuthenticationFailed):
#         response = Response({'detail': 'Authentication credentials were not provided.'},
#                             status=status.HTTP_401_UNAUTHORIZED)
#
#         return response
#     elif isinstance(exc, PermissionDenied):
#         response = Response({'detail': 'You do not have permission to perform this action.'},
#                             status=status.HTTP_403_FORBIDDEN)
#
#         return response