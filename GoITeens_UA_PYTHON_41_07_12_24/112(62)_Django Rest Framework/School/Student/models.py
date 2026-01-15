from django.db import models

# Create your models here.


class Cabinet(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)


class Subject(models.Model):
    name = models.CharField(max_length=50)


class Student(models.Model):
    full_name = models.CharField(max_length=250)
    age = models.IntegerField()
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE, related_name="students")
    subjects = models.ManyToManyField(Subject, related_name="students")


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="grades")
    grade = models.FloatField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="grades")
