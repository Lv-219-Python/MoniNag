<<<<<<< 16e921982f891290f7c743d408b82dda51df83a7
from hashlib import md5
=======
>>>>>>> Added initial backend part for user registration
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class CustomUser(AbstractBaseUser):
    first_name  = models.CharField(max_length=254, blank=True)
    second_name = models.CharField(max_length=254, blank=True)
    email       = models.EmailField(blank=True, unique=True)
    is_active    = models.BooleanField(default=False)
    is_admin     = models.BooleanField(default=False)
    is_staff     = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
<<<<<<< 16e921982f891290f7c743d408b82dda51df83a7
    avatar       =  models.CharField(default='', max_length=1000, editable=False)
=======
>>>>>>> Added initial backend part for user registration


    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

<<<<<<< 16e921982f891290f7c743d408b82dda51df83a7
    def save(self, *args, **kwargs):
        """
        Creates md5 hash from user email for gravatar integration and stores it in DB
        """
        cleaned_email = self.email.strip().lower().encode('utf-8')
        self.avatar = md5(cleaned_email).hexdigest()
        super(AbstractBaseUser, self).save(*args, **kwargs)
=======



>>>>>>> Added initial backend part for user registration
