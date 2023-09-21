from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password, first_name="", last_name=""):
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.is_superuser = False
        user.is_staff = False
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()
        return user


class User(AbstractUser):
    """Custom user model."""
    username = None
    email = models.EmailField(
        verbose_name='Email Address',
        max_length=255,
        unique=True,
    )

    first_name = models.CharField(
        verbose_name='First Name',
        max_length=150,
        blank=True,
    )

    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=150,
        blank=True,
    )

    date_joined = models.DateTimeField(
        verbose_name='Date when user account was created.',
        auto_now_add=True,
        editable=False,
    )

    is_active = models.BooleanField(
        verbose_name='Is user account activated',
        default=False,
    )

    otp_counter = models.PositiveIntegerField(
        verbose_name='OTP counter',
        default=0,
        editable=False,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
