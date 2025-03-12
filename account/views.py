from account.serializers import SessionTokenObtainSerializer
from rest_framework.decorators import permission_classes, action
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserSerializer

class SessionTokenObtainPairView(TokenObtainPairView):
    serializer_class = SessionTokenObtainSerializer


class UserProfileViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(status=201)

        return Response(serializer.errors, status=400)


    def update(self, request, pk=None):
        pass
    


"""
class OnlyAuthenticatedUserView(APIView): 
    permission_classes = [ss]

    authentication_classes = [JWTAuthentication]

    def get(self, request):
        user = request.user
        print(f"user 정보: {user}")
        if not user:
            return Response({"error": "접근 권한이 없습니다."}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({"message": "Accepted"})
"""