from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='john@example.com',
            first_name='John',
            last_name='Connor',
            password='12345',
        )

    def test_unique_email_is_enforced(self):
        """Test that two users with same email are not allowed."""
        with self.assertRaises(IntegrityError):
            User.objects.create(
                email=self.user.email,
                password='12345',
            )

    def test_date_joined_added_on_create(self):
        """Test that the date is automatically saved on creation."""
        self.assertTrue(isinstance(self.user.date_joined, datetime))

    def test_create_user_only_with_required_fields(self):
        """Test that user can be created with required fileds only."""
        try:
            User.objects.create(
                email='sara@example.com',
                password='12345',
            )
        except:
            self.fail(f"Object has not been created.")
