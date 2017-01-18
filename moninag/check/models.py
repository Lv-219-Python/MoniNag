from django.db import models

# Create your models here.

class Check(models.Model):

	name = models.CharField(max_length=20)
	plugin_name = models.CharField(max_length=20)
	run_freq = models.IntegerField()

	def __str__(self):
		return "Check Name: %s, Plugin Name: %s, Run Frequency: %d".format(self.name,
                                                    					   self.plugin_name,
                                                    					   self.run_freq)
