"""This module contains custom validators"""

import re

def validate_dict(dictionary, requirements):
    """Validate given dictionary for required keys.

    Args:
        dictionary(dict): Dictionary to validate.
        requirements(set): Set of required keys in dictionary.

    Returns:
        bool: The return value. True if valid, False otherwise.
    """

    return not bool(requirements ^ set(dictionary.keys()))


def validate_subdict(dictionary, requirements):
    """Validate given dictionary to be a subset of requirements.

    Args:
        dictionary(dict): Dictionary to validate.
        requirements(set): Set of required keys in dictionary.

    Returns:
        bool: The return value. True if valid, False otherwise.
    """

    return set(dictionary.keys()).issubset(requirements)

def validate_email(email):
    """Validate given dictionary to be a subset of requirements.

    Args:
        email(str): Email adress to validate.

    Returns:
        bool: The return value. True if valid, False otherwise.
    """

    result = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    return True if result else False
