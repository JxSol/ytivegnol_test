from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for User objects."""
    url = serializers.HyperlinkedIdentityField(
        view_name='users:user-detail',
        lookup_field='pk',
    )

    password = serializers.CharField(
        write_only=True,
        required=True,
    )

    is_active = serializers.BooleanField(
        write_only=True,
        default=False,
    )

    class Meta:
        model = User
        fields = (
            'url',
            'email',
            'password',
            'first_name',
            'last_name',
            'is_active',
            'date_joined',
        )
        read_only_fields = (
            'url',
            'date_joined',
        )

    def create(self, validated_data) -> User:
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class ResetPasswordSerializer(serializers.Serializer):
    """Serializer for reset password."""
    current_password = serializers.CharField(
        write_only=True,
        required=True,
    )

    new_password = serializers.CharField(
        write_only=True,
        required=True,
    )
