from django.db import models

# Create your models here.

class Vacines(models.Model):
    date = models.DateField(
        blank=False,
        null=False,
    )

    vacine = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )

    dose = models.IntegerField(
        max_length=3,
        blank=False,
        null=False,
    )

    batch = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )

    vaccinator = models.CharField(
        max_length=200,
        blank=False,
        null=False,
    )

    objects = models.Manager()

