from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from microblog.views.twit_comment import TweetCommentsAPIView
from microblog.views.register import RegisterAPIView
from microblog.views.comments import CreateCommentsAPIView, DeleteCommentAPIView, UpdateCommentAPIView
from microblog.views.twits import TwitsAPIView
from microblog.views.twits_for_id import TwitsForIdAPIView
from microblog.views.profile import UserProfileAPIView
from django.conf import settings
from django.conf.urls.static import static
from microblog.views.subsciber import SubscribeAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/twits/', TwitsAPIView.as_view()),
    path('api/twits/<int:pk>/', TwitsForIdAPIView.as_view()),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/register/', RegisterAPIView.as_view()),


    path('api/twits/comments/', CreateCommentsAPIView.as_view()),
    path('api/twits/comments/delete/<int:pk>/', DeleteCommentAPIView.as_view()),
    path('api/twits/comments/update/<int:pk>/', UpdateCommentAPIView.as_view()),

    path('api/twits/<int:pk>/comments/', TweetCommentsAPIView.as_view()),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),

    path('api/profile/<username>/', UserProfileAPIView.as_view()),
    path('api/profile/<username>/edit/', UserProfileAPIView.as_view()),

    path('api/follow/', SubscribeAPIView.as_view())
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
