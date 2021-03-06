from django.contrib.gis.db import models
from django.contrib.gis.geos.collections import LineString
from django.contrib.auth.models import User


class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    owner = models.ForeignKey(
        User,
        verbose_name="owner",
        on_delete=models.CASCADE,
        default=1
    )
    activity_type = models.CharField(
        max_length=100,
        verbose_name="activity_type"
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    route = models.LineStringField(verbose_name="route",
                                   default=LineString)
    distance = models.FloatField(verbose_name="length", default=0)
