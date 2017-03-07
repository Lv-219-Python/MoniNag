"""This module contains Registration model class and basic functions"""

from hashlib import md5

from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class CustomUser(AbstractBaseUser):
    """
    Custom User
    with such fields:
        firstname
        secondname
        email
        is_active/is_admin/is_staff/is_superuser
        avatar
        activation-key
    """

    first_name = models.CharField(max_length=254, blank=True)
    second_name = models.CharField(max_length=254, blank=True)
    email = models.EmailField(blank=False, unique=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    avatar = models.CharField(default='', max_length=1000, editable=False)
    activation_key = models.CharField(default='', max_length=1000, editable=False)

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        """Returns the first_name plus the last_name, with a space in between."""

        full_name = '{} {}'.format(self.first_name, self.second_name)
        return full_name

    def save(self, *args, **kwargs):
        """Creates md5 hash from user email for gravatar integration and stores it in DB."""

        self.email = self.email.strip().lower()
        self.avatar = md5(self.email.encode('utf-8')).hexdigest()
        super(AbstractBaseUser, self).save(*args, **kwargs)

    def update(self, first_name=None, second_name=None, ):
        """Update user data.

        Args:
            first_name(str, optional): user first name. Defaults to None.
            second_name(str, optional): user second name. Defaults to None.
        """

        if first_name:
            self.first_name = first_name
        if second_name:
            self.second_name = second_name

        self.save()

    @staticmethod
    def get_by_id(user_id):
        """Get user with given id.

        Args:
            id (int): user id.

        Returns:
            CustomUser: If user was found, and None otherwise.
        """

        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return None

        return user

    def to_dict(self):
        """Convert model object to dictionary.

        Return:
            dict:
                {
                    'id': id,
                    'first_name': first name,
                    'second_name': second name,
                    'email': email,
                    'avatar': avatar,
                }
        """

        return {
            'id': self.id,
            'first_name': self.first_name,
            'second_name': self.second_name,
            'email': self.email,
            'avatar': self.avatar,
        }
