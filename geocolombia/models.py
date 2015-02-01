from django.db import models

class State(models.Model):
	code = models.SmallIntegerField()
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return '%d %s' % (self.code, self.name)

	def cities(self):
		return City.objects.filter(state=self)

class City(models.Model):
	code = models.SmallIntegerField()
	name = models.CharField(max_length=50)
	state = models.ForeignKey('State')

	def __unicode__(self):
		return '%d %s' % (self.code, self.name)