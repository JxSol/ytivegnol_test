import base64

import pyotp
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail
from djoser.serializers import TokenCreateSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer

User = get_user_model()

class OTPSendAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = TokenCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.filter(email=serializer.data.get('email')).first()
            if user:
                user.otp_counter += 1
                user.save()
                key = base64.b32encode((user.email + settings.SECRET_KEY).encode())
                hotp = pyotp.HOTP(key)
                send_mail(
                    subject=f"Account authentication on {{ site_name }}",
                    message=hotp.at(user.otp_counter),
                    from_email=None,
                    recipient_list=[user.email],
                )
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
