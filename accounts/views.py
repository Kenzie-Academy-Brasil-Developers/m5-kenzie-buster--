from rest_framework.views import APIView, Request, Response, status
from .serializers import UserSerializer, CustomJWTSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import UsersDetailsPermission
from django.shortcuts import get_object_or_404
from .models import User


class UsersView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class UsersDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, UsersDetailsPermission]

    def get(self, request: Request, user_id: int) -> Response:
        get_user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, get_user)

        serializer = UserSerializer(get_user)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request: Request, user_id: int) -> Response:
        update_user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, update_user)

        serializer = UserSerializer(update_user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

class UsersLoginView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer