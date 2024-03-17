from django.test import TestCase
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            name="testuser",
            email="test@example.com",
            password="testpassword",
        )

    def test_profile_creation(self):
        profile = Profile.objects.create(
            user=self.user,
            favorite_cuisine="Italian",
            dietary_preferences="Vegetarian",
        )
        self.assertEqual(profile.favorite_cuisine, "Italian")
        self.assertEqual(profile.dietary_preferences, "Vegetarian")
