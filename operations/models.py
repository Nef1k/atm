from django.db import models

from auth_core.models import *


class OperationType(models.Model):
    name = models.CharField(max_length=50)


class Operation(models.Model):
    type = models.ForeignKey(to=OperationType, on_delete=models.SET_NULL, null=True)
    card = models.ForeignKey(to=Card, on_delete=models.CASCADE)
    param = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    date = models.DateTimeField()
