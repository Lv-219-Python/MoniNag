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


# views test


# def test_creating_custom_user(self):
#     _user = CustomUser()
#     _user.first_name = "TestName1"
#     _user.second_name = "TestSecondName1"
#     _user.email = "TEST1@test.test"
#     _user.save()

# def test_IsInstance(self):
#     self.assertIsInstance(self.user, CustomUser)

# def test_first_name(self):
#     self.assertEqual(self.user.first_name, "TestName")

# def test_second_name(self):
#     self.assertEqual(self.user.second_name, "TestSecondName")

# def test_email(self):
#     self.assertEqual(self.user.email, "TEST@test.test")
#     # Haven't used self.user.save() yet

# def test_avatar(self):
#     self.assertEqual(self.user.avatar, "avatar")

# def test_activation_key(self):
#     self.assertEqual(self.user.activation_key, 1)

# user = CustomUser.objects.get(email="test@test.test")
# user.save()
# self.assertEqual(user.avatar, "dd46a756faad4727fb679320751f6dea")
# # dd46a756... = md5 for "avatar"
# self.assertEqual(user.email, "test@test.test")
# # save() has email.strip().lower()


# _user = CustomUser.objects.get(user.id)

# user.assertEqual(first_name, 'TestName')
# self.assertEqual(second_name, 'TestSecondName')
# self.assertTrue(email.islower())


"""
Test that we can create a custom user
"""

# return CustomUser.objects.create(
#     first_name=first_name, second_name=second_name,
#     email=email, is_active=is_active, is_staff=is_staff,
#     is_superuser=is_superuser, avatar=avatar,
#     activation_key=activation_key, USERNAME_FIELD=USERNAME_FIELD
# )


# def test_get_full_name(self):
#     """
#     Test if we can get a full name of a user
#     """
#     full_name = '{} {}'.format("first_name", "second_name")
#     return full_name
