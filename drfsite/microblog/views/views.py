from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.authtoken.models import Token
from microblog.exceptions import TokenDoesNotExist


class LogoutView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user = request.user
        try:
            token = Token.objects.get(user=user)
        except TokenDoesNotExist:
            token = None
        if token:
            token.delete()
        return Response({"message": "Вы успешно вышли из системы."})
