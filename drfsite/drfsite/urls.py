"""
URL configuration for drfsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from microblog.views.twit_comment import TweetCommentsAPIView
from microblog.views.register import RegisterAPIView
from microblog.views.comments import CommentsAPIView
from microblog.views.twits import TwitsAPIView
from microblog.views.twits_for_id import TwitsForIdAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/twits/', TwitsAPIView.as_view()),
    path('api/twits/<int:pk>', TwitsForIdAPIView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/register/', RegisterAPIView.as_view()),
    path('api/register/<int:pk>', RegisterAPIView.as_view()),
    path('api/twits/comments/', CommentsAPIView.as_view()),
    path('api/twits/comments/<int:pk>/', CommentsAPIView.as_view()),
    path('api/twits/<int:pk>/comments/', TweetCommentsAPIView.as_view()),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]
