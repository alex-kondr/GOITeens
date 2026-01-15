from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    bio = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} р."
