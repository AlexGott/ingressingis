from django.db import models


class GEOPoint(models.Model):
    name = models.CharField(max_length=120)
    lat = models.IntegerField()
    lng = models.IntegerField()

    def __str__(self):
        return self.name
