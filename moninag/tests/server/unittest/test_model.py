from django.test import TestCase

from server.models import Server
from registration.models import CustomUser


class TestServer(TestCase):
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
        user = CustomUser.objects.get(id=1)
        data = {
            "name": "ServerName1",
            "address": "ServerAddress1",
            "state": "Production",
        }
        server = Server.create(user=user, **data)
        self.assertEqual(server, Server.objects.get(id=1))

    def test_update(self):
        server = Server.objects.get(id=2)
        server.update(name='TestName', address='127.0.0.1', state='Production')
        self.assertEqual(Server.objects.get(id=2).name, 'TestName')
        self.assertEqual(Server.objects.get(id=2).address, '127.0.0.1')
        self.assertEqual(Server.objects.get(id=2).state, 'Production')

    def test_get_by_id(self):
        test1 = Server.get_by_id(2)
        self.assertEqual(test1, Server.objects.get(pk=2))

    def test_get_by_id_none(self):
        test2 = Server.get_by_id(66)
        self.assertEqual(test2, None)

    def test_get_by_user_id(self):
        test = Server.get_by_user_id(1)
        self.assertEqual(len(test), 2)

    def test_to_dict(self):
        server = Server.objects.get(id=2)
        test = {
            'id': server.id,
            'name': server.name,
            'address': server.address,
            'state': server.state,
            'user_id': server.user.id
        }
        self.assertEqual(server.to_dict(), test)

    def test___str__(self):
        server = Server.objects.get(id=2)
        test = "ServerId: {}, ServerName: {}, ServerAddress: {}, ServerState {}".format(server.id,
                                                                                        server.name,
                                                                                        server.address,
                                                                                        server.state)

        self.assertEqual(str(server), test)
