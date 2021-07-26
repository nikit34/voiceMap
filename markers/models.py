from django.db import models
from django.contrib.gis.db.models import PointField


class Marker(models.Model):
    name = models.CharField(max_length=255)
    location = PointField()
