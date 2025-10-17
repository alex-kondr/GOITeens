from django.db import models

# Create your models here.


class Cabinet(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Кабінет: {self.name}"


class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Предмет: {self.name}"


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    bio = models.TextField()
    age = models.IntegerField()
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE, default=None, null=True)
    subjects = models.ManyToManyField(Subject, default=None)

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.cabinet}"
