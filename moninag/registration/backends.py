"""This module holds backend parts of registration"""

from registration.models import CustomUser


class CustomUserAuth(object):
    """Class which holds methods for Custom user authentication"""

    def authenticate(self, username=None, password=None):  # pylint: disable=no-self-use
        """
        User login method
        :param username: username (email)
        :param password: user password
        :return:
        """

        try:
            user = CustomUser.objects.get(email=username)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):  # pylint: disable=no-self-use
        """Get user by id

        :param user_id: id
        :return: User
        """

        try:
            user = CustomUser.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except CustomUser.DoesNotExist:
            return None
