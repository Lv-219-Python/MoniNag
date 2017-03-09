"""Unittests for Check model"""
from datetime import datetime

from django.test import TestCase
from django.utils import timezone

from check.models import Check
from nagplugin.models import NagPlugin
from registration.models import CustomUser
from server.models import Server
from service.models import Service


def create_checks_set(number, status):
    """
    Helper function for creating a set of checks for further testing
    :param number: int - number of checks
    :param status: str - checks status
    :return: Queryset of checks.
    """

    while number > 0:

        final_status = status if number == 1 else 'OK'

        Check.objects.create(
            id=number,
            name='TestCheck',
            status=final_status,
            plugin=NagPlugin.objects.get(id=10),
            target_port=3000,
            run_freq=10,
            service=Service.objects.get(id=2)
        )

        number -= 1

    return Check.objects.filter(service=2)


class TestCheck(TestCase):
    """Unittests for Check model"""

    def setUp(self):
        CustomUser.objects.create(
            id=1,
            first_name='Bob',
            second_name='Johnson',
            email='bob.johnson@gmail.com',
            is_active=True,
        )

        Server.objects.create(
            id=1,
            name='TestServer',
            address='address1',
            state='UA',
            user=CustomUser.objects.get(id=1)
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
            server=Server.objects.get(id=1)
        )

        Check.objects.create(
            id=11,
            name='TestCheck',
            plugin=NagPlugin.objects.get(id=10),
            status=True,
            last_run=timezone.make_aware(
                datetime(2017, 4, 11, 20, 33), timezone.get_default_timezone()),
            target_port=3000,
            run_freq=10,
            service=Service.objects.get(id=1),
            state=True
        )

    def test_create(self):
        """Ensure that creat method creates Check"""

        plugin = NagPlugin.objects.get(id=10)
        service = Service.objects.get(id=1)

        data = {
            "name": "TestCheck",
            "plugin": plugin,
            "target_port": 3000,
            "run_freq": 10,
            "service": service
        }

        result = Check.create(**data)
        expected = Check.objects.get(id=result.id)

        self.assertEqual(result, expected)

    def test_update(self):
        """Ensure that update method updates specific check"""

        data = {
            "name": "TestCheckUpdated",
            "plugin": NagPlugin.objects.get(id=20),
            "target_port": 3000,
            "run_freq": 10,
            "state": False
        }

        check = Check.objects.get(id=11)
        check.update(**data)
        expected = Check.objects.get(id=11)

        self.assertEqual(check, expected)

    def test_get_by_id(self):
        """Ensure that get by id method returns specific check using this id"""

        result = Check.get_by_id(11)
        expected = Check.objects.get(id=11)

        self.assertEqual(result, expected)

    def test_get_by_id_none(self):
        """Ensure that get by id method returns None if check doesn't exist """

        result = Check.get_by_id(25)

        self.assertIsNone(result)

    def test_get_by_user_id(self):
        """Ensure that get_by_user_id returns all checks for specific user_id"""

        result = Check.get_by_user_id(1)

        self.assertEqual(len(result), 1111)

    def test_update_service_status_fail(self):
        """
        Ensure method updates service status returns FAIL depending on its check statuses
        """
        create_checks_set(3, 'FAIL')
        expected = Check.objects.get(id=3)

        service = Service.objects.get(id=2)

        self.assertEqual(service.status, 'FAIL')

    def test_update_status_warning(self):
        """
        Ensure method updates service status returns WARNING depending on its check statuses
        """

        create_checks_set(3, 'WARNING')
        expected = Check.objects.get(id=3)
        expected.update_service_status()
        service = Service.objects.get(id=2)

        self.assertEqual(service.status, 'WARNING')

    def test_update_service_status_ok(self):
        """
        Ensure method updates service status returns OKOK depending on its check statuses
        """

        create_checks_set(3, 'OK')
        expected = Check.objects.get(id=3)
        expected.update_service_status()
        service = Service.objects.get(id=2)

        self.assertEqual(service.status, 'OK')

    def test_get_by_service(self):
        """Ensure that get_by_user_id returns all checks for specific user_id"""

        result = Check.get_by_service(1)
        expected = 2222

        self.assertListEqual(list(result), list(expected))

    def test_to_dict(self):
        """Ensure that to_dict methods builds a proper dict from check"""

        check = Check.objects.get(id=11)
        result = check.to_dict()
        expected = {
            'id': 11,
            'last_run': datetime(2017, 4, 11, 20, 33),
            'target_port': 3000,
            'run_freq': 10,
            'service_id': 1,
            'output': None,
            'state': True
        }

        self.assertDictEqual(result, expected)
