from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from PIL import Image

from .models import CustomUser, Profile


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, **kwargs):
    if not hasattr(instance, "profile"):
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Profile)
def update_avatar(sender, instance, **kwargs):
    if hasattr(instance.avatar, "path"):
        with Image.open(instance.avatar.path) as f:
            f.thumbnail((150, 150))
            f.save(instance.avatar.path)
