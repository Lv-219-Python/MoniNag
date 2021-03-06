"""This module contains Unit Tests for Service app models"""

from django.test import TestCase

from service.models import Service
from server.models import Server
from registration.models import CustomUser


class ServiceTest(TestCase):
    """Tests for Service model"""

    def setUp(self):
        user = CustomUser.objects.create(id=1,
                                         first_name="firstname",
                                         second_name="secondname",
                                         email="email@gmail.com")

        user2 = CustomUser.objects.create(id=3,
                                          first_name="firstname3",
                                          second_name="secondname3",
                                          email="email3@gmail.com")

        server = Server.objects.create(id=1,
                                       name="name",
                                       address="address",
                                       state="Production",
                                       user=user)

        server2 = Server.objects.create(id=2,
                                        name="name2",
                                        address="address2",
                                        state="Production",
                                        user=user2)

        Service.objects.create(id=20,
                               name="service1",
                               status="ok",
                               server=server2)

        Service.objects.create(id=30,
                               name="service2",
                               status="Fail",
                               server=server2)

        Service.objects.create(id=40,
                               name="service3",
                               status="Fail",
                               server=server)

    def test_service_update(self):
        """Ensure that update method updates service"""

        ser1 = Service.objects.get(name="service1")
        ser1.update(name="service2")
        self.assertEqual(ser1.name, "service2")

    def test_service_create(self):
        """Ensure that create method creates service"""

        server = Server.objects.get(id=1)
        Service.create("service_new", server, "ok")
        service = Service.objects.get(name="service_new")

        self.assertEqual(service.name, "service_new")
        self.assertEqual(service.status, "ok")
        self.assertEqual(service.server, server)

    def test_service_get_by_id(self):
        """Ensure that get by id method returns service with specific id"""

        actual = Service.objects.get(id=30)
        expect = Service.get_by_id(30)
        self.assertEqual(expect, actual)

    def test_service_get_by_server_id(self):
        """Ensure that get by server id method
        returns services of server with specific id"""

        server = Server.objects.get(id=1)
        actual = Service.objects.filter(server=server)
        expect = Service.get_by_server_id(1)
        self.assertQuerysetEqual(expect, map(repr, actual), ordered=False)

    def test_service_get_by_user_id(self):
        """Ensure that get by user id method
        returns services of user with specific id"""

        actual = Service.objects.filter(server__user__id=3)
        expect = Service.get_by_user_id(3)
        self.assertQuerysetEqual(expect, map(repr, actual), ordered=False)

    def test_service_get_by_statuses(self):
        """Ensure that get by statuses method
        returns services with specific statuses"""

        actual = Service.objects.filter(status__in=["ok"])
        expect = Service.get_by_statuses(["ok"])
        self.assertQuerysetEqual(expect, map(repr, actual), ordered=False)

    def test_service_to_dict(self):
        """Ensure that to_dict methods
        creates a proper dict from service"""

        service = Service.objects.get(id=30)
        actual = {
            'id': 30,
            'name': "service2",
            'status': "Fail",
            'state': True,
            'server_id': 2
        }
        expect = service.to_dict()
        self.assertEqual(expect, actual)

    def test_service__str__(self):
        """Ensure that __str__ method
        creates a proper str representation of a service"""

        service = Service.objects.get(id=20)
        actual = 'Service id: 20, name: service1, status: ok'
        expect = service.__str__()
        self.assertEqual(expect, actual)
