from django.db import models

STATE_CHOICES = (
    (1, "NotSelected"),
    (2, "Production"),
    (3, "Staging"),
)


class Server(models.Model):
    """
    Server Model
    Fields:
        id:         Integer - AutoField (primary key)
        name:       String - Server name
        address:    String - Server address (ipv4/ipv6/...)
        state:      String - production state (production/staging/...)
        user_id:    Integer - user_id for this server
    """
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=100, choices=STATE_CHOICES, default=0)

    def __str__(self):
        return "ServerId: {}, ServerName: {}, ServerAddress: {}, ServerStatus {}".format(self.id,
                                                                                         self.name,
                                                                                         self.address,
                                                                                         self.status)

