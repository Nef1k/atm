from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import CardManager

# Create your models here.


class Card(AbstractBaseUser):
    number = models.IntegerField(primary_key=True)
    pin = models.IntegerField()
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    auth_attempts_failed = models.IntegerField()

    is_active = models.BooleanField()

    objects = CardManager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'number'

    def get_full_name(self):
        return self.number


class AuthAttempt(models.Model):
    card = models.ForeignKey(to=Card, on_delete=models.CASCADE)
    attempt_date = models.DateTimeField()
