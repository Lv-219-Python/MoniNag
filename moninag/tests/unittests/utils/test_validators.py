from django.test import TestCase

import utils.validators as validator


class TestServer(TestCase):
    def test_validate_dict_sucess(self):
        """Ensure that validate_dict method returns TRUE if data fits requirements"""

        requirements = {'a', 'b', 'c'}
        data = {'a': 1, 'b': 2, 'c': 'test'}
        result = validator.validate_dict(data, requirements)

        self.assertTrue(result)

    def test_validate_dict_fail(self):
        """Ensure that validate_dict method returns FALSE if data doesn't fit requirements"""

        requirements = {'a', 'b', 'c'}
        data = {'a': 1, 'x': 2}
        result = validator.validate_dict(data, requirements)

        self.assertFalse(result)

    def test_validate_subdict_sucess(self):
        """Ensure that validate_dict method returns TRUE if data is a subset of requirements"""

        requirements = {'a', 'b', 'c'}
        data = {'a': 1, 'b': 2}
        result = validator.validate_subdict(data, requirements)

        self.assertTrue(result)

    def test_validate_subdict_fail(self):
        """Ensure that validate_dict method returns TRUE if data is a subset of requirements"""

        requirements = {'a', 'b', 'c'}
        data = {'a': 1, 'x': 2}
        result = validator.validate_subdict(data, requirements)

        self.assertFalse(result)
