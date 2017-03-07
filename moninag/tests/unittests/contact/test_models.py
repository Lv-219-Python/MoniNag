"""This module contains Unit Tests for Contact app models"""

from django.test import TestCase

from contact.models import Contact
from registration.models import CustomUser


class ContactTest(TestCase):
    """Tests for contacts"""

    def setUp(self):
        """Tests for Contact model"""

        CustomUser.objects.create(
            id=1,
            first_name='jacob',
            second_name='jacob1',
            email='jacob@…',
            is_active=True)

        CustomUser.objects.create(
            id=2,
            first_name='jacob1',
            second_name='jacob2',
            email='jacob2@…',
            is_active=True)

        Contact.objects.create(
            id=3,
            first_name='first_name',
            second_name='second_name',
            email='email1234@gmail.com',
            is_active=True,
            user=CustomUser.objects.get(id=1))

        Contact.objects.create(
            id=4,
            first_name='first_name1',
            second_name='second_name1',
            email='emailZVX@gmail.com',
            user=CustomUser.objects.get(id=1))

        Contact.objects.create(
            id=5,
            first_name='2first_name1',
            second_name='2second_name1',
            email='emailasdx@gmail.com',
            user=CustomUser.objects.get(id=2))

    def test_updating(self):
        """Ensure that update method updates specific contact."""

        contact = Contact.objects.get(id=3)
        contact.update(
            first_name='new_first_name',
            second_name='new_second_name',
            email='new_email@gmail.com')

        result = Contact.objects.get(id=3)

        self.assertEqual(result.first_name, 'new_first_name')
        self.assertEqual(result.second_name, 'new_second_name')
        self.assertEqual(result.email, 'new_email@gmail.com')

    def test_get_by_id_is_none(self):
        """Ensure that get_by_id method returns none if contact does not exist."""

        result = Contact.get_by_id(None)

        self.assertIsNone(result)

    def test_get_by_id(self):
        """Ensure that get_by_id method returns contact with specific id."""

        result = Contact.get_by_id(3)
        self.assertEqual(result, Contact.objects.get(id=3))

    def test_get_by_user_id(self):
        """Ensure that get_by_user_id returns all servers for specific user_id."""

        result = Contact.get_by_user_id(1)
        self.assertQuerysetEqual(result, map(repr, Contact.objects.filter(user=1)), ordered=False)

    def test_to_dict(self):
        """Ensure that to_dict methods builds a proper dict from contact"""

        result = Contact.objects.get(id=3).to_dict()
        expected = {
            'id': 3,
            'first_name': 'first_name',
            'second_name': 'second_name',
            'email': 'email1234@gmail.com',
            'is_active': True
        }

        self.assertDictEqual(expected, result)
