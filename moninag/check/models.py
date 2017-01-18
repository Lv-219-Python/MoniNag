from django.db import models

# Create your models here.

class Check(models.Model):

	check_name = models.CharField(max_length = 20)
	check_plugin_name = models.CharField(max_length = 20)
	check_run_freq = models.IntegerField()

	def __str__(self):
		return "<Check Name: %s, Plugin Name: %s, Run Frequency: %d>".format(self.check_name, self.check_plugin_name, self.check_run_freq)