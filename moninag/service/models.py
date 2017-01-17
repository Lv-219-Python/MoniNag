from django.db import models


class Service(models.Model):
    """
    Service model class

    name    - service name
    status  - service status
    server  - foreign key to server which owns service (many-to-one)
    """

    name = models.CharField(default="", max_length=200)
    status = models.CharField(default="", max_length=50)

    def __str__(self):
        return "Service id: {}, name: {}, status: {}, server: {}".format(self.id,
                                                                         self.name,
                                                                         self.status)
