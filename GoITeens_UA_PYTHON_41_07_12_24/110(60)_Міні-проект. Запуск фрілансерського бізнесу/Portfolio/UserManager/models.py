from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефону", null=True, default=None, help_text="Введіть номер телефону")
    bio = models.TextField(verbose_name="Інформація про себе", help_text="Опиши свій досвід", null=True, default=None)
    avatar = models.ImageField(upload_to=".", verbose_name="Фото профілю", help_text="Вибери своє фото", null=True, default=None)
    telegram = models.CharField(max_length=50, verbose_name="Нік у телеграм", help_text="Має починатись із символа '@'", null=True, default=None)
    viber = models.CharField(max_length=20, verbose_name="Номер телефону у viber", help_text="Введіть номер телефону viber для зв'язку", null=True, default=None)
    github = models.URLField(max_length=255, verbose_name="Посилання на профіль у GitHub", help_text="Введіть посиланя на профіль GitHub", null=True, default=None)

    def __str__(self):
        return f"{self.user.get_full_name()}: {self.phone_number}"
