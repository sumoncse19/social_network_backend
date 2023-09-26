from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# TokenObtainPairView --> To get access and refresh tokens
# TokenRefreshView --> For refreshing that token

from . import api

urlpatterns = [
  path('me/', api.me, name='me'),
  path('signup/', api.signup, name='signup'),
  path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
  path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
