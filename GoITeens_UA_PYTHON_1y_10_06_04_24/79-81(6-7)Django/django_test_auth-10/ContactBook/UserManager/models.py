from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class MySuperUser(AbstractUser):
    phone_number = models.CharField(max_length=16, null=True, blank=True, default=None)
    address = models.CharField(max_length=200, null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
