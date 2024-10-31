from django.db import models

# Create your models here.

class TBLusuarios(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    username = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    senha = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

objetos = models.Manager()