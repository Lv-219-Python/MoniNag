from django.db import models

class Check(models.Model):
    check_id = models.IntegerField(primary_key=True)
    check_name = models.CharField(max_length=20)
    check_plugin_name = models.CharField(max_length=20)
    check_run_freq = models.IntegerField()

