import base64

import pyotp
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from djoser.serializers import TokenCreateSerializer
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for User objects."""
    password = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
            'first_name',
            'last_name',
            'date_joined',
        )
        read_only_fields = (
            'id',
            'date_joined',
        )

class OTPTokenCreateSerializer(TokenCreateSerializer):
    otp = serializers.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        otp = attrs.get('otp')
        key = base64.b32encode((self.user.email + settings.SECRET_KEY).encode())
        hotp = pyotp.HOTP(key)
        if hotp.verify(otp, self.user.otp_counter):
            return attrs
        self.fail("invalid_credentials")