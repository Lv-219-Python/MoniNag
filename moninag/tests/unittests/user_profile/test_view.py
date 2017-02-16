import json

from django.core.urlresolvers import reverse
from django.test import Client, mock, TestCase

from registration.models import CustomUser


class FakeMD5(object):
    """Mock md5 function from hashlib."""

    def __init__(self, *args, **kwargs):
        pass

    def hexdigest(self):
        return 'fake_avatar_md5_hash'


class TestUserProfileView(TestCase):

    @mock.patch('registration.models.md5', FakeMD5)
    def setUp(self):

        CustomUser.objects.create(
            id=1,
            first_name='Luke',
            second_name='Skywalker',
            email='test1@gmail.com',
            is_active=True,
        )

        self.user = CustomUser.objects.create(
            id=2,
            first_name='Harry',
            second_name='Potter',
            email='test2@gmail.com',
            is_active=True,
        )
        self.user.set_password('password')
        self.user.save()

        self.client = Client()
        self.client.login(username='test2@gmail.com', password='password')

    def test_get(self):
        """Ensure that GET method returns signed up user profile and 200 status."""

        expected_json = json.dumps({
            'response': {
                'id': 2,
                'first_name': 'Harry',
                'second_name': 'Potter',
                'email': 'test2@gmail.com',
                'avatar': 'fake_avatar_md5_hash',
            }
        })

        url = reverse('user_profile')
        response = self.client.get(url)

        recieved_json = response.content.decode('utf-8')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(recieved_json, expected_json)

    def test_get_id(self):
        """Ensure that GET method returns user profile with given id and 200 status."""

        expected_json = json.dumps({
            'response': {
                'id': 1,
                'first_name': 'Luke',
                'second_name': 'Skywalker',
                'email': 'test1@gmail.com',
                'avatar': 'fake_avatar_md5_hash',
            }
        })

        url = reverse('user_profile_id', args=[1])
        response = self.client.get(url)

        recieved_json = response.content.decode('utf-8')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(recieved_json, expected_json)

    def test_get_not_existing_id(self):
        """Ensure that GET method returns error if user id does not exist and 404 status."""

        expected_json = json.dumps({
            'error': 'User with specified id was not found.',
        })

        url = reverse('user_profile_id', args=[3])
        response = self.client.get(url)

        recieved_json = response.content.decode('utf-8')

        self.assertEqual(response.status_code, 404)
        self.assertJSONEqual(recieved_json, expected_json)

    @mock.patch('registration.models.md5', FakeMD5)
    def test_put_all_fields(self):
        """Ensure that PUT method returns fully updated user profile and 200 status."""

        new_data_json = json.dumps({
            'first_name': 'New',
            'second_name': 'Name',
        })

        expected_json = json.dumps({
            'response': {
                'id': 2,
                'first_name': 'New',
                'second_name': 'Name',
                'email': 'test2@gmail.com',
                'avatar': 'fake_avatar_md5_hash',
            }
        })

        url = reverse('user_profile')
        response = self.client.put(url, new_data_json)

        recieved_json = response.content.decode('utf-8')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(recieved_json, expected_json)

    @mock.patch('registration.models.md5', FakeMD5)
    def test_put_not_all_fields(self):
        """Ensure that PUT method returns partially updated user profile and 200 status."""

        new_data_json = json.dumps({
            'first_name': 'New',
        })

        expected_json = json.dumps({
            'response': {
                'id': 2,
                'first_name': 'New',
                'second_name': 'Potter',
                'email': 'test2@gmail.com',
                'avatar': 'fake_avatar_md5_hash',
            }
        })

        url = reverse('user_profile')
        response = self.client.put(url, new_data_json)

        recieved_json = response.content.decode('utf-8')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(recieved_json, expected_json)

    def test_put_invalid_json(self):
        """Ensure that PUT method returns error if JSON is invalid and 400 status."""

        new_data = {
            'bad_key': 'New',
            'second_name': 'Name',
        }

        expected_json = json.dumps({
            'error': 'Incorrect JSON format.',
        })

        url = reverse('user_profile')
        response = self.client.put(url, json.dumps(new_data))

        recieved_json = response.content.decode('utf-8')

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(recieved_json, expected_json)
