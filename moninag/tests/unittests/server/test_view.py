import json
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse
from django.test import Client
from django.test import TestCase

from server.models import Server
from registration.models import CustomUser


# Helper functions

def to_dict(server):
    """Convert model object to dictionary.

    :return: dict:
            {
                'id': id,
                'name': name,
                'address': address.
                'state': state,
                'user_id': user.id
            }
    """

    return {
        'id': server.id,
        'name': server.name,
        'address': server.address,
        'state': server.state,
        'user_id': server.user.id
    }


class TestServerView(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            id=1,
            first_name='Frank',
            second_name='Sinatra',
            email='testemail@gmail.com',
            is_active=True,
        )
        self.user.set_password('password')
        self.user.save()
        self.user = authenticate(username='testemail@gmail.com', password='password')

        CustomUser.objects.create(
            id=2,
            first_name='Leonard',
            second_name='Cohen',
            email='testemail2@gmail.com',
            is_active=True,
        )

        Server.objects.create(
            id=1,
            name='Google.com',
            address='google.com',
            state='test',
            user=CustomUser.objects.get(id=1)
        )

        Server.objects.create(
            id=3,
            name='SS',
            address='softserve.ua',
            state='test',
            user=CustomUser.objects.get(id=1)
        )

        Server.objects.create(
            id=4,
            name='SSac',
            address='softserve.academy',
            state='test',
            user=CustomUser.objects.get(id=2)
        )

        self.client = Client()
        self.client.login(username='testemail@gmail.com', password='password')

    def test_get_servers(self):
        """Ensure that GET method returns all servers for authenticated user"""

        url = reverse('servers')
        response = self.client.get(url)

        # Create expected result
        servers = Server.objects.filter(user=1)
        expected_json_response = {}
        expected_json_response['response'] = [to_dict(server) for server in servers]

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content.decode('utf-8'), expected_json_response)

    def test_get_server(self):
        """Ensure that GET method returns specific server for authenticated user"""

        url = reverse('server', args=[1])
        response = self.client.get(url)

        # Create expected specific server response
        expected_json_response = {}
        server = Server.objects.get(id=1)
        expected_json_response['response'] = to_dict(server)

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content.decode('utf-8'), expected_json_response)

    def test_get_server_permission_denied(self):
        """Ensure that GET for server which doesn't belong to authenticated user returns 403 status"""

        url = reverse('server', args=[4])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 403)

    def test_get_not_existing_server(self):
        """Ensure that GET for server which does not exist returns 404 status"""

        url = reverse('server', args=[55])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_post(self):
        """Ensure that POST method creates server with specified data"""

        url = reverse('servers')
        data = json.dumps({'name': 'ServerName',
                           'address': 'Server.com',
                           'state': 'Production'})

        response = self.client.post(url, data=data, content_type='application/json')
        server = Server.objects.get(id=2)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(server.name, 'ServerName')
        self.assertEqual(server.address, 'Server.com')
        self.assertEqual(server.state, 'Production')
        self.assertEqual(server.user.id, 1)

    def test_post_incorrect_format(self):
        """Ensure that PUT fails to create server with invalid data on input and returns 404"""

        url = reverse('servers')
        data = json.dumps({'name': 'ServerName',
                           'address': 'Server.com'})

        response = self.client.post(url, data=data, content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_put(self):
        """Ensure that PUT method updates server properly and returns 200"""

        url = reverse('server', args=[1])
        data = json.dumps({'name': 'NewName',
                           'address': 'test.com',
                           'state': 'Staging'})

        response = self.client.put(url, data=data, content_type='application/json')
        server = Server.objects.get(id=1)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(server.name, 'NewName')
        self.assertEqual(server.address, 'test.com')
        self.assertEqual(server.state, 'Staging')

    def test_put_incorrect_format(self):
        """Ensure that PUT method fails to update server with incorrect input data format and returns 400"""

        url = reverse('server', args=[4])
        data = json.dumps({'name': 'NewName',
                           'addr': 'test.com',
                           'state': 'Staging'})

        response = self.client.put(url, data=data, content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_put_not_existing_server(self):
        """Ensure that PUT method fails to update not existing server and returns 404"""

        url = reverse('server', args=[111])
        data = json.dumps({'name': 'NewName',
                           'address': 'test.com',
                           'state': 'Staging'})

        response = self.client.put(url, data=data, content_type='application/json')

        self.assertEqual(response.status_code, 404)

    def test_put_permission_denied(self):
        """Ensure that PUT method fails to update server with another user owner and returns 403"""

        url = reverse('server', args=[4])
        data = json.dumps({'name': 'NewName',
                           'address': 'test.com',
                           'state': 'Staging'})

        response = self.client.put(url, data=data, content_type='application/json')

        self.assertEqual(response.status_code, 403)

    def test_delete(self):
        """Ensure that DELETE method deletes server with specified id and returns 200"""

        url = reverse('server', args=[1])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Server.objects.all()), 2)

    def test_delete_permission_denied(self):
        """Ensure that DELETE method fails to delete server with another user owner and returns 403"""

        url = reverse('server', args=[4])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 403)

    def test_delete_not_existing_server(self):
        """Ensure that DELETE method fails to delete not existing server and returns 404"""

        url = reverse('server', args=[44])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 404)

