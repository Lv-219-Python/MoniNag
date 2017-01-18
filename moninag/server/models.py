from django.db import models

STATUS_CHOICES = (
    (1, ("NotSelected")),
    (2, ("Production")),
    (3, ("Staging")),
)


class Server(models.Model):
    """
    Server model with fields:
    id, name, address, status
    """
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return "ServerId: {}, ServerName: {}, ServerAddress: {}, ServerStatus {}".format(self.id,
                                                                                         self.name,
                                                                                         self.address,
                                                                                         self.status)