from django.db import models


class Run(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="name"
    )
    created = models.DateTimeField(
        auto_now_add=True
    )


class Activity(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    username = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="username"
    )
    activity_type = models.CharField(
        max_length=100,
        verbose_name="activity_type"
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
