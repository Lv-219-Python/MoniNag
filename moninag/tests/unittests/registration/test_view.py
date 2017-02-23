from django.core.urlresolvers import reverse
from django.test import Client
from django.test import TestCase

from registration.models import CustomUser


class CustomUserTest(TestCase):
    """
    Tests for CustomUser model
    """
    def setUp(self):
        CustomUser.objects.create(first_name="TestName",
                                  second_name="TestSecondName",
                                  email="test@test.test",
                                  avatar="avatar")

    def test_full_name(self):

        """Ensure that get_full_name method works properly"""

        user = CustomUser.objects.get(email="test@test.test")
        self.assertEqual(user.get_full_name(), "TestName TestSecondName")

    def test_save(self):

        """Ensure that save() method works properly, changing email address to lower()"""

        user = CustomUser()
        user.first_name = "Firstname"
        user.second_name = "secondmn"
        user.email = "TESTmail@test.so"
        user.avatar = "avatartest"
        user.save()

        self.assertEqual(user.email, "testmail@test.so")

    def test_save_rewrite(self):

        """Ensure that we can update user's variables"""

        user = CustomUser.objects.get(email="test@test.test")
        user.first_name = "UpdatedName"
        user.save()
        actual_user = CustomUser.objects.get(email="test@test.test")
        self.assertEqual(actual_user.first_name, "UpdatedName")
