from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import Users, UserDetail, SignUp, AboutMe

urlpatterns = [
    path('api/v1/users/me/', AboutMe.as_view(), name='about_me'),
    path('api/v1/users/', Users.as_view()),
    path('api/v1/users/<str:username>/', UserDetail.as_view()),
    path('api/v1/auth/email/', SignUp.as_view(), name='confirmation_code'),
    path('api/v1/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
