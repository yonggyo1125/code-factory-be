from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from account.views import SessionTokenObtainPairView, UserProfileViewSet

router = DefaultRouter()
router.register(r'account', UserProfileViewSet, basename="account")



urlpatterns = [
    path('token/', SessionTokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('',include(router.urls)),

]