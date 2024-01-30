
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from microblog.validators.username_email import validators_username_email

from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.permissions import AllowAny
from microblog.serializers.register import RegisterSerializer


@extend_schema_view(
    create=extend_schema(
        summary="Регистрация нового пользователя",
    ),
)
class RegisterAPIView(APIView):
    """
    Описание представления RegisterAPIView.
    """
    permission_classes = [AllowAny,]

    @extend_schema(
        summary="Регистрация нового пользователя",
        request=RegisterSerializer,
        responses={
            201: {'description': 'User registered successfully'},
            400: {'description': 'Invalid request data'}
        }
    )
    def post(self, request):
        """
        Регистрация нового пользователя.
        """
        user = RegisterSerializer(data=request.data)
        if user.is_valid():
            validation_response = validators_username_email(username=request.data['username'],
                                                            email=request.data['email'])
            if validation_response is not None:
                return validation_response

            user.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

    # @extend_schema(
    #     summary="Удаление пользователя по идентификатору",
    #     responses={
    #         204: {'description': 'User deleted successfully'},
    #         404: {'description': 'User not found'}
    #     }
    # )
    # def delete(self, request, pk):
    #     """
    #     Удаление пользователя по идентификатору.
    #     """
    #     try:
    #         user = CustomUser.objects.get(pk=pk)
    #         user.delete()
    #         return Response({'detail': 'User deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    #     except ObjectDoesNotExist:
    #         return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)