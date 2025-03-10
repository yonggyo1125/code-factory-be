from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

#from .views import OnlyAuthenticatedUserView
from account.views import SessionTokenObtainPairView, UserProfileViewSet

urlpatterns = [
    path('token/', SessionTokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('account/', UserProfileViewSet.as_view(), name="account")
    #path("authonly/", OnlyAuthenticatedUserView.as_view())
]