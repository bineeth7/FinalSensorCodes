from django.db import models

# Create your models here.
class Data(models.Model):
    rainfall = models.FloatField(max_length=30)
    vibration = models.FloatField(max_length=3)
    moisture = models.FloatField(max_length=5)
    status = models.IntegerField()

    def __str__(self):
        return self.name