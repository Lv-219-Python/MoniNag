from django.core.urlresolvers import reverse
from django.test import Client

# imports for views

from registration.models import CustomUser
from django.test import TestCase

# imports for everything


# models test


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
        user = CustomUser.objects.get(email="test@test.test")
        self.assertEqual(user.get_full_name(), "TestName TestSecondName")

    def test_save(self):
        user = CustomUser()
        user.first_name = "Firstname"
        user.second_name = "secondmn"
        user.email = "TESTmail@test.so"
        user.avatar = "avatartest"
        user.save()

        self.assertEqual(user.email, "testmail@test.so")

    def test_save_rewrite(self):
        user = CustomUser.objects.get(email="test@test.test")
        user.first_name = "UpdatedName"
        user.save()
        actual_user = CustomUser.objects.get(email="test@test.test")
        self.assertEqual(actual_user.first_name, "UpdatedName")


# views test will be here someday
