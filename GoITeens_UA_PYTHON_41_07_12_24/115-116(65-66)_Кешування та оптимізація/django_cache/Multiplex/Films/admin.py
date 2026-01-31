from django.contrib import admin

from .models import Category, Actor, Film, Review

# Register your models here.


admin.site.register([Category, Actor, Film, Review])
