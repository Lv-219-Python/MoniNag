from django.db import models

from service.models import Service


class Check(models.Model):
    """
    Check model class

    name            define name of check
    plugin          define name of plugin
    run_freq        define time value of runing time
    target_port     define value of port
    id              set by default, foreign key to service
    """

    name = models.CharField(max_length=20, default=0)
    plugin_name = models.CharField(max_length=20, default=0)
    target_port = models.IntegerField(default=0)
    run_freq = models.IntegerField(default=0)
    service = models.ForeignKey(Service)

    def __str__(self):
        return "Check Name: {}, Plugin Name: {}, Run Frequency: {}, Port: {}".format(self.name,
                                                                                     self.plugin_name,
                                                                                     self.run_freq,
                                                                                     self.target_port)
