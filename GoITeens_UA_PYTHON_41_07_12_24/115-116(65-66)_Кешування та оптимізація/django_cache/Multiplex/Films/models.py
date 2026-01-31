from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва категорії")
    age_limit = models.PositiveIntegerField(default=3, verbose_name="Вікові обмеження")

    def __str__(self):
        return f"Категорія: {self.name} ({self.age_limit}+)"


class Actor(models.Model):
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Актор: {self.full_name}"


class Film(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва фільму")
    description = models.TextField(max_length=1000, verbose_name="Опис фільму", default=None, null=True, blank=True)
    rating = models.DecimalField(verbose_name="Рейтинг фільму", default=5, max_digits=2, decimal_places=1)
    timing = models.PositiveIntegerField(verbose_name="Тривалість фільму у хвилинах")
    categories = models.ManyToManyField(Category, verbose_name="Категорії")
    actors = models.ManyToManyField(Actor, verbose_name="Актори")
    quality = models.CharField(default=None, null=True, blank=True, verbose_name="Якість", max_length=255)
    release = models.DateTimeField(verbose_name="Дата виходу", default=None, null=True, blank=True)
    poster = models.ImageField(upload_to=".", default=None, null=True, blank=True, verbose_name="Постер")

    def __str__(self):
        return f"Фільм: {self.name}"


class Review(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name="Фільм")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач")
    review = models.TextField(max_length=5000, verbose_name="Відгук")
    rating = models.DecimalField(verbose_name="Оцінка", decimal_places=1, max_digits=2)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата відгуку")

    def __str__(self):
        return f"Відгук від {self.user.username} на фільм {self.film.name}"
