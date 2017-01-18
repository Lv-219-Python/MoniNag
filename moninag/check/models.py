from django.db import models


class Check(models.Model):
    """
    Check model class

    name      define name of check
    plugin    define name of plugin
    run_freq  define time value of runing time
    id        set by default, foreign key to service
    """

    name = models.CharField(max_length=20, default=0)
    plugin_name = models.CharField(max_length=20, default=0)
    run_freq = models.IntegerField(default=0)

    def __str__(self):
        return "Check Name: %s, Plugin Name: %s, Run Frequency: %d".format(self.name,
                                                                           self.plugin_name,
                                                                           self.run_freq)
