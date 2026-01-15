from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Picture(models.Model):
    picture = models.ImageField(upload_to=".", verbose_name="Фото проекту")


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pictures = models.ManyToManyField(Picture)
    github = models.URLField(max_length=255, verbose_name="Посилання на проект", help_text="Введіть посилання GitHub проекту")
    description = models.TextField(verbose_name="Опис проекту", help_text="Опишіть Ваш проект", null=True, default=None)
    name = models.CharField(max_length=255, verbose_name="Назва проекту", help_text="Введіть назву свого проекту")
    dockerhub = models.URLField(max_length=255, verbose_name="Посилання на DockerHub", help_text="Введіть посилання DocketHub контейнера зі своїм проектом (за бажанням)", null=True, default=None)
