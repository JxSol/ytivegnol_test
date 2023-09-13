from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response

from .serializers import UserSerializer, ResetPasswordSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """API viewset for User management."""
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == 'reset_password':
            return ResetPasswordSerializer
        return UserSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action in ('list', 'retrieve', 'destroy'):
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(
        url_path='me',
        methods=['GET', 'PATCH', 'DELETE'],
        detail=False,
    )
    def me(self, request):
        user = request.user
        serializer = self.get_serializer_class()(user, context={'request': request})

        if request.method == 'GET':
            return Response(serializer.data, status.HTTP_200_OK)

        if request.method == 'PATCH':
            serializer.partial = True
            serializer.data = request.data
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_200_OK)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    @action(
        url_path='reset_password',
        methods=['POST'],
        detail=False,
    )
    def reset_password(self, request):
        user = request.user
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid():
            if check_password(request.data['current_password'], user.password):
                user.set_password(request.data['new_password'])
                user.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(
                {'detail': 'Wrong password'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
