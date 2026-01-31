from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    bio = models.CharField(max_length=1000, null=True, blank=True, default=None, verbose_name="Біографія", help_text="Розкажи про себе...")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефону", null=True, blank=True, default=None)
    place = models.CharField(max_length=255, null=True, blank=True, default=None, verbose_name="Вкажіть місце проживання")


class Profile(models.Model):
    avatar = models.ImageField(upload_to=".", verbose_name="Аватарочка", null=True, default=None, blank=True)
    hobby = models.CharField(max_length=255, null=True, default=None, blank=True, verbose_name="Улюблена справа")
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
