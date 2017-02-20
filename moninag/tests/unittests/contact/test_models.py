from django.test import TestCase

from contact.models import Contact
from registration.models import CustomUser


class ContactTest(TestCase):

    def setUp(self):

        CustomUser.objects.create(
            id=1,
            first_name='jacob',
            second_name='jacob1',
            email='jacob@…')

        CustomUser.objects.create(
            id=2,
            first_name='jacob1',
            second_name='jacob2',
            email='jacob2@…')

        Contact.objects.create(
            id=3,
            first_name='first_name',
            second_name='second_name',
            email='email@gmail.com',
            user=CustomUser.objects.get(id=1))

        Contact.objects.create(
            id=4,
            first_name='first_name1',
            second_name='second_name1',
            email='email1@gmail.com',
            user=CustomUser.objects.get(id=1))

        Contact.objects.create(
            id=5,
            first_name='2first_name1',
            second_name='2second_name1',
            email='email2@gmail.com',
            user=CustomUser.objects.get(id=2))

    def test_create(self):

        user = CustomUser.objects.get(id=1)

        data = {'first_name': 'first_name',
                'second_name': 'second_name',
                'email': 'email5@gmail.com'}

        result = Contact.create(user=user, **data)
        expected = Contact.objects.get(id=1)

        self.assertEqual(result, expected)

    def test_updating(self):

        contact = Contact.objects.get(id=3)
        contact.update(
            first_name='new_first_name',
            second_name='new_second_name',
            email='new_email@gmail.com')

        result = Contact.objects.get(id=3)

        self.assertEqual(result.first_name, 'new_first_name')
        self.assertEqual(result.second_name, 'new_second_name')
        self.assertEqual(result.email, 'new_email@gmail.com')

    def test_get_by_id_is_None(self):

        result = Contact.get_by_id(None)

        self.assertIsNone(result)

    def test_get_by_id(self):

        result = Contact.get_by_id(3)

        self.assertEqual(result, Contact.objects.get(id=3))

    def test_get_by_user_id(self):

        result = Contact.get_by_user_id(1)

        self.assertEqual(len(result), 2)

    def test_to_dict(self):

        contact = Contact.objects.get(id=3)
        result = contact.to_dict()
        expected = {
            'id': 3,
            'first_name': 'first_name',
            'second_name': 'second_name',
            'email': 'email@gmail.com'
        }

        self.assertEqual(result, expected)
