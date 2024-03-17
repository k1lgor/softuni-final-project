from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class UserManagerTest(TestCase):

    def test_create_user(self):
        # Create a user instance
        user = User.objects.create_user(
            email="normal@user.com", name="normal user", password="foo"
        )

        # Check that the user has been correctly created
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)
        self.assertEqual(user.email, "normal@user.com")
        self.assertEqual(user.name, "normal user")

        # Check that the password has been correctly set
        self.assertTrue(user.check_password("foo"))

    def test_create_user_no_email_raises_error(self):
        # Try to create a user without an email and expect a ValueError
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", name="user without email")

    def test_create_user_no_name_raises_error(self):
        # Try to create a user without a name and expect a ValueError
        with self.assertRaises(ValueError):
            User.objects.create_user(email="user@without.name", name="")

    def test_create_superuser(self):
        # Create a superuser instance
        superuser = User.objects.create_superuser(
            email="super@user.com", name="super user", password="foo"
        )

        # Check that the superuser has been correctly created
        self.assertIsInstance(superuser, User)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_active)
        self.assertEqual(superuser.email, "super@user.com")
        self.assertEqual(superuser.name, "super user")

        # Check that the password has been correctly set
        self.assertTrue(superuser.check_password("foo"))
