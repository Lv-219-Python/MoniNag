from django.test import TestCase

from nagplugin.models import NagPlugin


class TestPlugin(TestCase):
    def test_get_by_id(self):
        """Ensure that get by id method returns specific plugin using id"""

        result = NagPlugin.get_by_id(1)
        expected = NagPlugin.objects.get(id=1)

        self.assertEqual(result, expected)

    def test_get(self):
        """Ensure that get method returns all plugins"""

        result = NagPlugin.get()
        expected = NagPlugin.objects.all()[0:20]

        self.assertQuerysetEqual(result, map(repr, expected), ordered=False)

    def test_get_by_id_none(self):
        """Ensure that get_by_id method returns none if plugin does not exist"""

        result = NagPlugin.get_by_id(66)
        self.assertIsNone(result)

    def test_get_by_name(self):
        """Ensure that get_by_name returns all plugins for specific name"""

        result = NagPlugin.get_by_name("check_dns")
        expected = NagPlugin.objects.filter(name="check_dns")
        self.assertQuerysetEqual(result, map(repr, expected))

    def test_to_dict(self):
        """Ensure that to_dict methods builds a proper dict from plugin"""

        plugin = NagPlugin.objects.get(id=1)
        result = plugin.to_dict()
        expected = {
            'id': 1,
            'name': 'check_dns',
            'template': '/usr/lib/nagios/plugins/check_dns -H {host}',
            'description': ''
        }

        self.assertDictEqual(result, expected)

    def test___str__(self):
        """Ensure that __str__ method builds a proper str representation of a plugin"""

        plugin = NagPlugin.objects.get(id=1)
        result = str(plugin)
        expected = 'Plugin id: {}, name: {}, template: {}, description: {}'.format(plugin.id,
                                                                                   plugin.name,
                                                                                   plugin.template,
                                                                                   plugin.description)

        self.assertEqual(result, expected)
