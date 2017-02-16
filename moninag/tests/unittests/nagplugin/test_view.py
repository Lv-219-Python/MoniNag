import json

from django.core.urlresolvers import reverse
from django.test import Client, TestCase

from nagplugin.models import NagPlugin
from registration.models import CustomUser


class TestNagPluginView(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            id=1,
            first_name='Frank',
            second_name='Sinatra',
            email='test@test.com',
            is_active=True,
        )
        self.user.set_password('password')
        self.user.save()
        self.client = Client()
        self.client.login(username='test@test.com', password='password')

    def test_get_plugin(self):
        """Ensure that GET method returns specific plugins for authenticated user and 200 status"""

        url = reverse('nagplugins')
        response = self.client.get(url)

        # Create expected specific plugins response
        expected_json_response = {}
        plugins = NagPlugin.get()
        expected_json_response['response'] = [plugin.to_dict() for plugin in plugins]
        expected_json_response = json.dumps(expected_json_response)

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content.decode('utf-8'), expected_json_response)
