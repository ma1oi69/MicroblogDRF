from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from microblog.serializers.user_profile import UserProfileSerializer
from microblog.models.user import CustomUser
from microblog.exceptions import UserNotExists
from django.contrib.auth.hashers import check_password


class UserProfileAPIView(APIView):

    def get(self, request, pk):
        try:
            user_profile = CustomUser.objects.get(id=pk)
            serializer = UserProfileSerializer(user_profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserNotExists:
            return Response('Profile user not found', status=status.HTTP_404_NOT_FOUND)


class ChangePasswordAPIView(APIView):

    def post(self, request, pk):
        user = request.user
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')

        if not check_password(old_password, user.password):
            return Response('Старый пароль указан неверно', status=status.HTTP_400_BAD_REQUEST)

        if old_password == new_password:
            return Response('Новый пароль совпадает со старым паролем', status=status.HTTP_400_BAD_REQUEST)

        if check_password(new_password, user.password):
            return Response('Новый пароль совпадает с предыдущим паролем', status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()

        return Response('Пароль успешно изменен', status=status.HTTP_200_OK)


