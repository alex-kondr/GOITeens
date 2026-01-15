from django.db import models

from Author.models import Author

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f"Tag: {self.name}"


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, default=None)
    name = models.CharField(max_length=50, verbose_name="Назва статті")
    description = models.CharField(max_length=500, verbose_name="Короткий опис")
    text = models.TextField(verbose_name="Стаття")
    create_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"Стаття: {self.name} - автор: {self.author.first_name} {self.author.last_name}"
