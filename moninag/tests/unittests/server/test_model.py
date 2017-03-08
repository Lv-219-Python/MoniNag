"""This module contains Unit Tests for Server app models"""

from django.test import TestCase

from registration.models import CustomUser
from server.models import Server


class TestServer(TestCase):
    """Tests for Contact view"""

    def setUp(self):
        CustomUser.objects.create(
            id=1,
            first_name="Frank",
            second_name="Sinatra",
            email="TestEmail@gmail.com",
            is_active=True,
        )

        CustomUser.objects.create(
            id=2,
            first_name="Leonard",
            second_name="Cohen",
            email="TestEmail2@gmail.com",
            is_active=True,
        )

        Server.objects.create(
            id=2,
            name="Server2",
            address="address2",
            state="NotSelected",
            user=CustomUser.objects.get(id=1)
        )

        Server.objects.create(
            id=3,
            name="Server3",
            address="address3",
            state="Production",
            user=CustomUser.objects.get(id=1)
        )

        Server.objects.create(
            id=4,
            name="Server4",
            address="address4",
            state="Staging",
            user=CustomUser.objects.get(id=2)
        )

    def test_create(self):
        """Ensure that creat method craetes server"""

        user = CustomUser.objects.get(id=1)
        data = {
            "name": "ServerName1",
            "address": "ServerAddress1",
            "state": "Production"
        }

        result = Server.create(user=user, **data)
        expected = Server.objects.get(id=1)

        self.assertEqual(result, expected)

    def test_get_by_id(self):
        """Ensure that get by id method returns specific server using id"""

        result = Server.get_by_id(2)
        expected = Server.objects.get(id=2)

        self.assertEqual(result, expected)

    def test_update(self):
        """Ensure that update method updates specific server"""

        server = Server.objects.get(id=2)
        server.update(name='TestName', address='127.0.0.1', state='Production')
        result = Server.objects.get(id=2)

        self.assertEqual(result.name, 'TestName')
        self.assertEqual(result.address, '127.0.0.1')
        self.assertEqual(result.state, 'Production')

    def test_get_by_id_none(self):
        """Ensure that get_by_id method returns none if server does not exist"""

        result = Server.get_by_id(66)
        self.assertEqual(result, None)

    def test_get_by_user_id(self):
        """Ensure that get_by_user_id returns all servers for specific user_id"""

        result = Server.get_by_user_id(1)
        self.assertEqual(len(result), 2)

    def test_to_dict(self):
        """Ensure that to_dict methods builds a proper dict from server"""

        server = Server.objects.get(id=2)
        result = server.to_dict()
        expected = {
            'id': 2,
            'name': "Server2",
            'address': "address2",
            'state': "NotSelected",
            'user_id': 1
        }

        self.assertDictEqual(result, expected)

    def test___str__(self):
        """Ensure that __str__ method builds a proper str representation of a server"""

        server = Server.objects.get(id=2)
        result = str(server)
        expected = 'ServerId: {}, ServerName: {}, ServerAddress: {},' \
                   ' ServerState {}'.format(server.id,
                                            server.name,
                                            server.address,
                                            server.state)

        self.assertEqual(result, expected)
