"""Unittests for Check views"""
import json

from django.core.serializers.json import DjangoJSONEncoder
from django.test import TestCase, Client
from django.urls import reverse

from check.models import Check
from nagplugin.models import NagPlugin
from registration.models import CustomUser
from server.models import Server
from service.models import Service


# Helper function
def to_dict(check):
    """Convert model object to dictionary.

    :return: dict:
            {
                'id': check id,
                'name': check name,
                'plugin_id': nagios plugin id,
                'status': status,
                'last_run': last run,
                'output': output,
                'target_port': target port,
                'run_freq': run frequency,
                'service_id': service id,
                'state': state
            }
    """

    return {
        'id': check.id,
        'name': check.name,
        'plugin_id': check.plugin.id,
        'plugin_name': check.plugin.name,
        'status': check.status,
        'last_run': check.last_run,
        'output': check.output,
        'target_port': check.target_port,
        'run_freq': check.run_freq,
        'service_id': check.service.id,
        'state': check.state,
    }


class TestCheckView(TestCase):
    """Unittests for Check views"""

    def setUp(self):
        self.user1 = CustomUser.objects.create(
            id=1,
            first_name='Bob',
            second_name='Johnson',
            email='bob.johnson@gmail.com',
            is_active=True,
        )

        self.user2 = CustomUser.objects.create(
            id=2,
            first_name='Sven',
            second_name='Johanson',
            email='sven.johanson@gmail.com',
            is_active=True,
        )

        self.user1.set_password('password')
        self.user1.save()

        Server.objects.create(
            id=1,
            name='TestServer',
            address='address1',
            state='UA',
            user=CustomUser.objects.get(id=1)
        )

        Server.objects.create(
            id=2,
            name='TestServer user 2',
            address='address2',
            state='US',
            user=CustomUser.objects.get(id=2)
        )

        NagPlugin.objects.create(
            id=10,
            name='TestPlugin',
            template='TestTemplate'
        )

        NagPlugin.objects.create(
            id=20,
            name='TestPlugin_2',
            template='TestTemplate_2'
        )

        Service.objects.create(
            id=1,
            name='TestService',
            status='ok',
            server=Server.objects.get(id=1)
        )

        Service.objects.create(
            id=2,
            name='TestService_2',
            status='fail',
            server=Server.objects.get(id=2)
        )

        Check.objects.create(
            id=11,
            name='TestCheck',
            plugin=NagPlugin.objects.get(id=10),
            status=True,
            last_run='2017-04-01 23:13',
            target_port=3000,
            run_freq=10,
            service=Service.objects.get(id=1),
            state=True
        )

        Check.objects.create(
            id=12,
            name='TestCheck 2',
            plugin=NagPlugin.objects.get(id=10),
            status=True,
            last_run='2017-04-01 23:13',
            target_port=2342,
            run_freq=23,
            service=Service.objects.get(id=2),
            state=True
        )

        self.client = Client()
        self.client.login(username='bob.johnson@gmail.com', password='password')

    def test_get_check_not_found(self):
        """Ensure that GET method returns check not found message and 404 status."""

        expected_json = json.dumps({
            'error': 'Check with specified id was not found.'
        })

        url = reverse('check', args=[45])
        response = self.client.get(url)

        received_json = response.content.decode('utf-8')

        self.assertEqual(response.status_code, 404)
        self.assertJSONEqual(received_json, expected_json)

    def test_get_all_checks(self):
        """Ensure that GET method returns list of checks
        if no check id was passed as parameter to the url."""

        url = reverse('check')

        response = self.client.get(url)
        received_json = response.content.decode('utf-8')

        expected_response = {}

        checks = Check.objects.filter(service__server__user__id=1)
        expected_response['response'] = [to_dict(check) for check in checks]

        expected_json = json.dumps(expected_response, cls=DjangoJSONEncoder)

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(received_json, expected_json)

    def test_get_check(self):
        """Ensure that GET method returns specific Check
        if this check was assigned to the user and user is logged in."""

        url = reverse('check', args=[11])

        response = self.client.get(url)
        received_json = response.content.decode('utf-8')

        expected_response = {}
        expected_response['response'] = to_dict(Check.objects.get(id=11))

        expected_json = json.dumps(expected_response, cls=DjangoJSONEncoder)

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(received_json, expected_json)

    def test_get_check_user_mismatch(self):
        """Ensure that GET method returns 403 status
        if the requested Check is assigned to improper user"""

        url = reverse('check', args=[12])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 403)

    def test_post_check_invalid_json(self):
        """Ensure that POST method returns invalid JSON error and status 400"""

        expected_json = json.dumps({
            'error': 'Incorrect JSON format.'
            })
        url = reverse('check')
        data = json.dumps({
            "plugin": "10",
            "run_freq": "15",
            "target_port": "3000",
            "state": False,
        })
        response = self.client.post(url, data=data, content_type='application/json')
        received_json = response.content.decode('utf-8')

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(received_json, expected_json)

    def test_post_plugin_not_found(self):
        """Ensure that POST method returns Plugin not found error and status 404"""

        expected_json = json.dumps({
            'response': 'Plugin with given id was not found.'
        })
        url = reverse('check')
        data = json.dumps({
            "name": "test",
            "plugin_id": "200",
            "run_freq": "15",
            "target_port": "3000",
            "service_id": "1",
        })
        response = self.client.post(url, data=data, content_type='application/json')
        received_json = response.content.decode('utf-8')

        self.assertEqual(response.status_code, 404)
        self.assertJSONEqual(received_json, expected_json)

    def test_post_service_not_found(self):
        """Ensure that POST method returns Service not found error and status 404"""

        expected_json = json.dumps({
            'response': 'Service with given id was not found.'
        })
        url = reverse('check')
        data = json.dumps({
            "name": "test",
            "plugin_id": "10",
            "run_freq": "15",
            "target_port": "3000",
            "service_id": "103",
        })
        response = self.client.post(url, data=data, content_type='application/json')
        received_json = response.content.decode('utf-8')

        self.assertEqual(response.status_code, 404)
        self.assertJSONEqual(received_json, expected_json)

    def test_post_check_user_mismatch(self):
        """Ensure that POST method returns 403 status
        if the requested Check is assigned to improper user"""

        url = reverse('check')

        data = json.dumps({
            "name": "test",
            "plugin_id": "10",
            "run_freq": "15",
            "target_port": "3000",
            "service_id": "2",
        })
        response = self.client.post(url, data=data, content_type='application/json')

        self.assertEqual(response.status_code, 403)

    def test_post_check(self):
        """Ensure that POST method returns 200 status and
        response message if the specific Check was created"""

        url = reverse('check')
        data = json.dumps({
            "name": "test post",
            "plugin_id": "10",
            "run_freq": 15,
            "target_port": 3000,
            "service_id": "1",
        })
        response = self.client.post(url, data=data, content_type='application/json')
        received_json = response.content.decode('utf-8')

        expected_response = {}
        expected_response['response'] = to_dict(Check.objects.get(id=2))

        expected_json = json.dumps(expected_response, cls=DjangoJSONEncoder)

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(received_json, expected_json)

    def test_delete_check_not_found(self):
        """Ensure that DELETE method returns 404 status if the specific Check doesn't exist"""

        url = reverse('check', args=[45])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 404)

    def test_delete_check(self):
        """Ensure that DELETE method deletes specific Check and returns 200 status"""

        url = reverse('check', args=[11])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 200)

    def test_delete_check_user_mismatch(self):
        """Ensure that DELETE method returns 403 status
        if the requested Check is assigned to improper user"""

        url = reverse('check', args=[12])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 403)

    def test_put_check_invalid_json(self):
        """Ensure that PUT method returns invalid JSON error and status 400"""

        expected_json = json.dumps({
            'error': 'Incorrect JSON format.'
        })
        url = reverse('check', args=[22])
        data = json.dumps({
            "plugin": "10",
            "run_freq": "15",
            "target_port": "3000",
            "state": False,
        })
        response = self.client.put(url, data=data, content_type='application/json')
        received_json = response.content.decode('utf-8')

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(received_json, expected_json)

    def test_put_check_plugin_not_found(self):
        """Ensure that PUT method returns Plugin not found error and status 404"""

        expected_json = json.dumps({
            'response': 'Plugin with given id was not found.'
        })
        url = reverse('check', args=[11])
        data = json.dumps({
            "name": "test",
            "plugin_id": "200",
            "run_freq": "15",
            "target_port": "3000",
            "state": False,
        })
        response = self.client.put(url, data=data, content_type='application/json')
        received_json = response.content.decode('utf-8')

        self.assertEqual(response.status_code, 404)
        self.assertJSONEqual(received_json, expected_json)

    def test_put_check(self):
        """Ensure that PUT method returns 200 status with
        response text in JSON format if the specific Check
        was updated"""

        url = reverse('check', args=[11])

        data = json.dumps({
            "name": "test",
            "plugin_id": "10",
            "run_freq": 15,
            "target_port": 356,
            "state": False,
        })

        response = self.client.put(url, data=data, content_type='application/json')

        received_json = response.content.decode('utf-8')

        expected_response = {}
        expected_response['response'] = to_dict(Check.objects.get(id=11))

        expected_json = json.dumps(expected_response, cls=DjangoJSONEncoder)

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(received_json, expected_json)

    def test_put_check_user_mismatch(self):
        """Ensure that PUT method returns 403 status
        if the requested Check is assigned to improper user"""

        url = reverse('check', args=[12])

        data = json.dumps({
            "name": "test",
            "plugin_id": "20",
            "run_freq": "15",
            "target_port": "3000",
            "state": False,
        })

        response = self.client.put(url, data=data)

        self.assertEqual(response.status_code, 403)

    def test_put_check_not_found(self):
        """Ensure that PUT method returns 404 status if the specific Check doesn't exist"""

        expected_json = json.dumps({
            'error': 'Check with given id was not found.'
        })
        url = reverse('check', args=[22])
        data = json.dumps({
            "name": "test",
            "plugin_id": "10",
            "run_freq": "15",
            "target_port": "3000",
            "state": False,
        })
        response = self.client.put(url, data=data, content_type='application/json')
        received_json = response.content.decode('utf-8')

        self.assertEqual(response.status_code, 404)
        self.assertJSONEqual(received_json, expected_json)
