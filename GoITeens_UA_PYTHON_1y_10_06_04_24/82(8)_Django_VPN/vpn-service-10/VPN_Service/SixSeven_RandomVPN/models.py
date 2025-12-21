from datetime import timedelta, datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def create_time_exp():
    return datetime.now() + timedelta(days=7)


class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Location: {self.name}"


class Subscription(models.Model):
    name = models.CharField(max_length=100, unique=True)
    list_of_service = models.CharField(max_length=50)
    locations = models.ManyToManyField(Location)
    price = models.FloatField()

    def __str__(self):
        return f"Name: {self.name} -> service: {self.list_of_service}"


class Service(models.Model):
    ipv_4_ext = models.GenericIPAddressField(unique=True, default=None, null=True)
    ipv_4_int = models.GenericIPAddressField(unique=True, default=None, null=True)
    ipv_6 = models.GenericIPAddressField(unique=True, default=None, null=True)
    subscription = models.ManyToManyField(Subscription, related_name="subs")
    exp_time = models.DateTimeField(default=create_time_exp)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription_active = models.ForeignKey(Subscription, on_delete=models.SET_NULL, default=None, null=True, related_name="subscription_active")
