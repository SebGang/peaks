from django.db import models


class Peaks(models.Model):
    name = models.CharField(max_length=50)
    lat = models.FloatField()
    long = models.FloatField()
    altitude = models.FloatField()

    def __str__(self):
        return self.name
