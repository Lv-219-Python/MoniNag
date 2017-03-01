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
        user.second_name = "Secondname"
        user.email = "TESTmail@test.so"
        user.avatar = "avatartest"
        user.save()

        self.assertEqual(user.email, "testmail@test.so")

    def test_save_rewrite(self):
        """Ensure that we can rewrite user's variables"""

        user = CustomUser.objects.get(email="test@test.test")
        user.first_name = "UpdatedName"
        user.save()
        actual_user = CustomUser.objects.get(email="test@test.test")

        self.assertEqual(actual_user.first_name, "UpdatedName")

    def test_update(self):
        """Ensure that we can update the first and second names"""

        user = CustomUser.objects.get(email="test@test.test")
        user.update(first_name="UpdatedName", second_name="UpdatedSecondName")

        self.assertEqual(user.first_name, "UpdatedName")
        self.assertEqual(user.second_name, "UpdatedSecondName")

    def test_get_by_id(self):
        """Check if we can get the user by id"""

        user = CustomUser.get_by_id(2)
        expected_user = CustomUser.objects.get(id=2)
        self.assertEqual(user, expected_user)

    def test_get_by_id_false(self):
        """Check if we get none if passed id was not found"""

        user = CustomUser.get_by_id(44444)

        self.assertIsNone(user)

    def test_to_dict(self):
        """Check if to_dict works properly"""

        user = CustomUser.objects.get(email="test@test.test")
        result = user.to_dict()
        expected = {
            'id': 7,
            'first_name': "TestName",
            'second_name': "TestSecondName",
            'email': "test@test.test",
            'avatar': "dd46a756faad4727fb679320751f6dea"
        }

        self.assertDictEqual(result, expected)
