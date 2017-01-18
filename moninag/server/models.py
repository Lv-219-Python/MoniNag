from django.db import models

class Server(models.Model):
    STATES = list(
        'production',
        'staging'
    )
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    status = models.CharField(choices=STATES, default=STATES.draft)
    #user = models.ForeignKey(User, unique=True)
