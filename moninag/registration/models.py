from hashlib import md5
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=254, blank=True)
    second_name = models.CharField(max_length=254, blank=True)
    email = models.EmailField(blank=False, unique=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    avatar =  models.CharField(default='', max_length=1000, editable=False)

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name

    def get_first_name(self):
        """
        Returns the first name for the user.
        """
        return self.first_name

    def save(self, *args, **kwargs):
        """
        Creates md5 hash from user email for gravatar integration and stores it in DB
        """
        self.email = self.email.strip().lower()
        self.avatar = md5(self.email.encode('utf-8')).hexdigest()
        super(AbstractBaseUser, self).save(*args, **kwargs)
