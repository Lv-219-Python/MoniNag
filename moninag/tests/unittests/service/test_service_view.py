import json

from django.core.urlresolvers import reverse
from django.test import Client, TestCase

from registration.models import CustomUser
from server.models import Server
from service.models import Service
from check.models import Check


class TestServiceView(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(
            id=1,
            first_name='Name',
            second_name='Surname',
            email='email@gmail.com',
            is_active=True,
        )

        self.user.set_password('qwerty')
        self.user.save()

        CustomUser.objects.create(
            id=2,
            first_name='name2',
            second_name='second_name2',
            email='email2@gmail.com',
            is_active=True,
        )

        Server.objects.create(
            id=10,
            name='Server1',
            address='address1',
            state='test',
            user=CustomUser.objects.get(id=1)
        )

        Server.objects.create(
            id=20,
            name='Server2',
            address='address2',
            state='test',
            user=CustomUser.objects.get(id=2)
        )

        Service.objects.create(
            id=11,
            name='Service1',
            status='ok',
            server=Server.objects.get(id=10)
        )

        Service.objects.create(
            id=22,
            name='Service2',
            status='fail',
            server=Server.objects.get(id=10)
        )

        Service.objects.create(
            id=33,
            name='Service3',
            status='ok',
            server=Server.objects.get(id=20)
        )

        self.client = Client()
        self.client.login(username='email@gmail.com', password='qwerty')

    def test_get_services(self):
        """Ensure that GET method returns all services 
        for authenticated user and 200 status"""

        url = reverse('service')
        actual_response = self.client.get(url)

        servers = Server.objects.filter(user=1)
        services = Service.objects.filter(server__in=servers)

        expected_response = {}
        expected_response['response'] = [service.to_dict()
                                         for service in services]
        expected_response = json.dumps(expected_response)
        
        self.assertEqual(actual_response.status_code, 200)
        self.assertJSONEqual(actual_response.content.decode('utf-8'),
                             expected_response)

    def test_get_service(self):
        """Ensure that GET method returns specific service
        for authenticated user and 200 status"""

        url = reverse('service', args=[11])
        actual_response = self.client.get(url)

        expected_response = {}
        service = Service.objects.get(id=11)
        checks = Check.objects.filter(service=service)
        data = service.to_dict()
        data['checks'] = [
            {
                'id': check.id,
                'name': check.name,
                'plugin_id': check.plugin.id,
                'plugin_name': check.plugin.name,
                'target_port': check.target_port,
                'run_freq': check.run_freq,
                'service_id': check.service.id,
            } for check in checks]

        expected_response['response'] = data
        expected_response = json.dumps(expected_response)

        self.assertEqual(actual_response.status_code, 200)
        self.assertJSONEqual(actual_response.content.decode('utf-8'),
                             expected_response)
        
    def test_get_not_existing_service(self):
        """Ensure that GET method returns 404 status
        if the service doesn't exist"""

        url = reverse('service', args=[44])
        actual_response = self.client.get(url)

        self.assertEqual(actual_response.status_code, 404)

    def test_get_not_user_service(self):
        """Ensure that GET method returns 403 status
        if the service doesn't belong to user"""

        url = reverse('service', args=[33])
        actual_response = self.client.get(url)

        self.assertEqual(actual_response.status_code, 403)

    def test_post(self):
        """Ensure that POST method updates server
        and returns 201 status"""

        url = reverse('service')
        data = json.dumps({'name': 'Service',
                           'status': 'ok',
                           'server_id': 10})
        actual_response = self.client.post(url, data=data,
                                           content_type='application/json')
        service = Service.objects.get(name='Service')
        expected_response = {}
        expected_response['response'] = service.to_dict()
        expected_response = json.dumps(expected_response)

        self.assertEqual(actual_response.status_code, 201)
        self.assertJSONEqual(actual_response.content.decode('utf-8'),
                             expected_response)

    def test_post_invalid_format(self):
        """Ensure that POST method returns 400 status
        if json has invalid format"""

        url = reverse('service')
        data = json.dumps({'name': 'Service'})

        actual_response = self.client.post(url, data=data,
                                           content_type='application/json')

        self.assertEqual(actual_response.status_code, 400)

    def test_post_not_existing_server(self):
        """Ensure that POST method returns 404 status
        if the server of the service doen't exist"""

        url = reverse('service')
        data = json.dumps({'name': 'Service101',
                           'status': 'ok',
                           'server_id': 30})

        actual_response = self.client.post(url, data=data,
                                           content_type='application/json')

        self.assertEqual(actual_response.status_code, 404)

    def test_post_not_user_server(self):
        """Ensure that POST method returns 403 status
        if the server of the service doesn't belong to user"""

        url = reverse('service')
        data = json.dumps({'name': 'Service101',
                           'status': 'ok',
                           'server_id': 20})

        actual_response = self.client.post(url, data=data,
                                           content_type='application/json')

        self.assertEqual(actual_response.status_code, 403)

    def test_put(self):
        """Ensure that PUT method creates a new service
        and returns 200 status"""

        url = reverse('service', args=[11])
        data = json.dumps({'name': 'Service101',
                           'status': 'fail'})

        actual_response = self.client.put(url, data=data,
                                          content_type='application/json')

        service = Service.objects.get(id=11)
        expected_response = {}
        expected_response['response'] = service.to_dict()
        expected_response = json.dumps(expected_response)

        self.assertEqual(actual_response.status_code, 200)
        self.assertJSONEqual(actual_response.content.decode('utf-8'),
                             expected_response)

    def test_put_invalid_format(self):
        """Ensure that PUT method returns 400 status
        if json has invalid format"""

        url = reverse('service', args=[11])
        data = json.dumps({'name': 'Service101',
                           'status': '15',
                           'user_id': 18})

        actual_response = self.client.put(url, data=data,
                                          content_type='application/json')

        self.assertEqual(actual_response.status_code, 400)

    def test_put_not_existing_service(self):
        """Ensure that PUT method returns 404 status
        if the service with given id doesn't exist"""

        url = reverse('service', args=[44])
        data = json.dumps({'name': 'Service101',
                           'status': 'ok'})

        actual_response = self.client.put(url, data=data,
                                          content_type='application/json')

        self.assertEqual(actual_response.status_code, 404)

    def test_put_not_user_service(self):
        """Ensure that PUT method returns 403 status
        if the service with given id doesn't belong to user"""

        url = reverse('service', args=[33])
        data = json.dumps({'name': 'Service101',
                           'status': 'ok'})

        actual_response = self.client.put(url, data=data,
                                          content_type='application/json')

        self.assertEqual(actual_response.status_code, 403)

    def test_delete(self):
        """Ensure that DELETE method deletes the service
        and returns 200 status"""

        url = reverse('service', args=[11])
        actual_response = self.client.delete(url)

        self.assertEqual(actual_response.status_code, 200)
        self.assertEqual(len(Service.objects.all()), 2)

    def test_delete_not_user_service(self):
        """Ensure that DELETE method doesnt delete the service
        and returns 403 status
        if this service doesn't belong to user"""

        url = reverse('service', args=[33])
        actual_response = self.client.delete(url)

        self.assertEqual(actual_response.status_code, 403)

    def test_delete_not_existing_service(self):
        """Ensure that DELETE method returns 404 status
        if the service doesn't exist"""

        url = reverse('service', args=[44])
        actual_response = self.client.delete(url)

        self.assertEqual(actual_response.status_code, 404)
