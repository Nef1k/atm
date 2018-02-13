from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import CardManager

# Create your models here.


class Card(AbstractBaseUser):
    number = models.IntegerField(max_length=16, primary_key=True)
    pin = models.IntegerField(max_length=4)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    auth_attempts_failed = models.IntegerField(max_length=1)

    is_active = models.BooleanField()

    objects = CardManager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'number'

    def get_full_name(self):
        return self.number


class AuthAttempt(models.Model):
    card = models.ForeignKey(to=Card)
    attempt_date = models.DateTimeField()
